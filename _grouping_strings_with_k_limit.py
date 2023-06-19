words = ['the', 'day', 'began', 'with', 'something', 'nice', 'and','sweet']

# given a limit k, concat elements in the word array using '-' and ensure the element not exceeding the k 
# cur = "the"
# cur_temp

def group_text(words, k):
    res = []
    i = 1
    cur = ''
    cur_prev = '' # to save a text group if adding new word > k 
    n = len(words)
    while i < n:
        # print(i)
        cur_prev = cur # hold in case goes over k 
        if cur == '':
            cur += words[i]
        else: 
            cur += '-'+words[i]

        if len(cur)==k:
            res.append(cur) 
            # if group found then reset the cur and cur prev to start new group 
            if i < n: 
                cur = ''
                cur_prev = ''
            else:
                break
            i+=1 # move to next word
        elif len(cur)>k: 
            res.append(cur_prev)
            cur = ''
            cur_prev = ''
            # i-=1 no need to go back one because i is still at the new words
        else: 
            i+=1 # move to next word to add more becuase it is still < k

    return res

result = group_text(words, 15)
print(result)

