# You are given a string thestring. Compress and encrypt it using the following algorithm: Begin with an empty strings, for each group of consecutive repeating characters in thestring:
# 1. If the group length is 1, append the character to s followed by 1
# 2. Otherwise, get the group's length y (the group only contains consecutive repeating characters), then get the hexadecimal representation of y, append the character to s followed by y
# 3.
# Reverse s and return it
# Function Description Complete the function compressAndEncrypt in the editor below. The function must state what must be returned or printed. compressAndEncrypt has the following parameter(s):
# thestring: a string
# Sample Input For Custom Testing: aaaaaaaaaaa Sample Output: ba

# def compressAndEncrypt(thestring):
#     compressed_string = ""
#     i = 0
#     n = len(thestring)

#     while i < n:
#         count = 1
#         while i + 1 < n and thestring[i] == thestring[i + 1]:
#             count += 1
#             i += 1
        
#         if count == 1:
#             compressed_string += thestring[i]
#         else:
#             compressed_string += thestring[i] + hex(count)[2:] # [2:] to remove the 0x prefix ie 15 -> 0xf -> f
        
#         i += 1

#     return compressed_string[::-1]  # Reverse the compressed string

#%%
def compressAndEncrypt(thestring):
    compressed_string = ""
    i = 0 # index to loop through thestring
    n = len(thestring)

    while i < n: 
        # calculate number of nearby repeats
        count = 1
        while i + 1 < n and thestring[i] == thestring[i + 1]:
            count += 1
            i += 1 # have to use while loop to increment i 
            
        if count == 1: 
            compressed_string += thestring[i]
        else:
            compressed_string += thestring[i]+hex(count)[2:]
        
        i+=1
        # print('count',count)

    return compressed_string[::-1]
        


# Example usage
thestring = "aaaaaaaaaaab"
compressed_and_encrypted = compressAndEncrypt(thestring)
print(compressed_and_encrypted)


# %%
