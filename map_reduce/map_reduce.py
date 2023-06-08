# Interesting Read, Google Page Rank: https://github.com/apache/spark/blob/master/examples/src/main/python/pagerank.py

def read_file(file_path):
    with open(file_path, 'r') as f:
        next(f) # skip the header 
        for line in f:
            row = line.strip().split()
            row[-1] = int(row[-1])
            yield row
            # use yield becuase not wanting to terminate the function


rows = read_file('data.txt')

# to print, but once the generator is used, it is gone
# for r in rows: 
#     print(r)

# ['1', 'www.baidu.com', 123213]
# ['1', 'www.tiktok.com', 312321]
# ['2', 'www.qq.com', 321312]
# ['3', 'www.google.com', 321321]


# q1: write a function to count the distinct url for each user, return in a dict
def count_unique_url_by_user(rows):
    dict = {}
    for i, j, j in rows: 
        if i not in dict: 
            dict[i] = {j}
        else:
            dict[i].add(j)
    
    for e, w in dict.items():
        dict[e] = len(w)
    
    return dict

url_count = count_unique_url_by_user(rows)
print(url_count)

# result {'1': 2, '2': 1, '3': 1}

# q2: write this process in map reduce
# map:
def mapper(line):
    # Split the line into columns
    user_id, url, _ = line.split()

    # Emit a key-value pair with user_id as the key and url as the value
    yield (user_id, url)

    #[('1', 'www.baidu.com'), ('1', 'www.tiktok.com'), ('2', 'www.qq.com'), ('3', 'www.google.com'))]


def reducer(user_id, urls): # url =  ['www.baidu.com', 'www.tiktok.com']
    # Count the unique urls for each user_id
    # note that this reduce takes array not set, so we need to convert it to set
    unique_urls = set(urls) 

    # Emit the user_id and the count of unique urls
    yield user_id, len(unique_urls) # it is ok to calculate len because the user is set to 1 person


# Read the input data file
with open('data.txt', 'r') as file:
    # Apply the mapper function to each line in the file
    mapped_data = [mapper(line) for line in file]

    # sort the mapped data by the keys (urls)
    sorted_data = sorted(mapped_data, key=lambda x: x[0])
    
    # simulation of mapredue shuffling, in real world, this is done by hadoop
    #Shuffle: Group the mapped data by user_id
    grouped_data = {}
    for user_id, url in mapped_data:
        grouped_data.setdefault(user_id, []).append(url)
    # grouped_data = {'1': ['www.baidu.com', 'www.tiktok.com'], '2': ['www.qq.com'], '3': ['www.google.com']}

    # also simulate the hadoop reducer
    # Apply the reducer function to each group
    reduced_data = [reducer(user_id, urls) for user_id, urls in grouped_data.items()]

# q3: get the count result every hour
# map:
# map:
def mapper(line):
    # Split the line into columns
    user_id, url, ms = line.split()
    hour = (ms//3600000) * 1000

    # Emit a key-value pair with user_id as the key and url as the value
    yield (hour, user_id), url # tuple can be used as key, here hour and user_id are keys

#reduce:
def reducer(hour_user_id, urls):
    # Count the unique urls for each user_id
    unique_urls = set(urls)
    hour = hour_user_id[0]
    user_id = hour_user_id[1]
    # Emit the user_id and the count of unique urls
    yield hour, user_id, len(unique_urls)

# Read the input data file
with open('data.txt', 'r') as file:
    # Apply the mapper function to each line in the file
    mapped_data = [mapper(line) for line in file]

    # sort the mapped data by the keys (urls)
    sorted_data = sorted(mapped_data, key=lambda x: x[0])
    # sorted_data = [((1000, '1'), 'www.baidu.com'), ((1000, '1'), 'www.tiktok.com'), ((2000, '2'), 'www.qq.com'), ((3000, '3'), 'www.google.com')]
    
    # simulation of mapredue shuffling, in real world, this is done by hadoop
    #Shuffle: Group the mapped data by user_id
    grouped_data = {}
    for key, val in mapped_data:
        grouped_data.setdefault(key, []).append(val)
    # grouped_data = {'1': ['www.baidu.com', 'www.tiktok.com'], '2': ['www.qq.com'], '3': ['www.google.com']}

    # also simulate the hadoop reducer
    # Apply the reducer function to each group
    reduced_data = [reducer(user_id, urls) for user_id, urls in grouped_data.items()]

    # not the key is (hour, user_id)

# q4: if the users visited too many urls, ram cannot handle 
# {'www.baidu.com': ['1', '2', '3'], 'www.tiktok.com': ['1', '2', '3'], 'www.qq.com': ['1', '2', '3'], 'www.google.com': ['1', '2', '3']}
# then convert to disctionary using user_id as key
# {'1': ['www.baidu.com', 'www.tiktok.com'], '2': ['www.qq.com'], '3': ['www.google.com']}
# map:
def mapper(line):
    # Split the line into columns
    user_id, url, _ = line.split()

    # Emit a key-value pair with user_id as the key and url as the value
    yield (user_id, url)

#reduce:
def reducer(url, user_ids):
    # change to use user_id as key, id: [url1, url2]
    
    yield user_id, urls

# Read the input data file
with open('data.txt', 'r') as file:
    # Apply the mapper function to each line in the file
    mapped_data = [mapper(line) for line in file]

    # sort the mapped data by the keys (urls)
    sorted_data = sorted(mapped_data, key=lambda x: x[0])

    after reduce, combine all the reduced data, to get {user_id: [url1, url2]}
    {user_id: len(set(x))} 
    # 1 has 100 visit of baidu

    # simulation of mapredue shuffling, in real world, this is done by hadoop
    #Shuffle: Group the mapped data by user_id
    