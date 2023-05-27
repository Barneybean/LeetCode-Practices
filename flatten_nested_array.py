#%%
def flatten_array(arr):
    res = []
    def helper(e):
        if isinstance(e, list):
            for i in e:
                helper(i)
        else:
            res.append(e)
    helper(arr)  
    return res    

arr = [1,2,3,[4,5,[6]]]
flattened = list(flatten_array(arr))
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]
# %%
