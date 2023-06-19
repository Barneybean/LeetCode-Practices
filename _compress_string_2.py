# given a string: '122233422', return [[1,1], [2,3], [3,2], [4,1], [2,2]], count of each connected same number 
#%%
def compressAndEncrypt(thestring):
    res = []
    i = 0 
    n = len(thestring)
    while i < n:
        cur_count = 1 
        while i < n - 1 and thestring[i] == thestring[i+1]:
            cur_count += 1
            i += 1
        res.append([int(thestring[i]), cur_count])

        i+=1
        
    return res


# Example usage
thestring = "122233422"
compressed_and_encrypted = compressAndEncrypt(thestring)
print(compressed_and_encrypted)
[[1,1], [2,3], [3,2], [4,1], [2,2]]


