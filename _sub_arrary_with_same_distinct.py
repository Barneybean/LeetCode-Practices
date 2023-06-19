# given arr of integers, count the number of subarrays that has the same total distinct values as the original array.

# 1,2,2,3,3,3,4
# 3+3+1 2 and 3 + 2 and 33 + 2 and 333
# 3+3+1 
# 3+3+1 



def countSubarraysWithDistinctValues(arr):
    # get count of each element   
    res = 1  
    h = {}
    for e in arr:
        h[e] = h.get(e,0)+1
    
    def formula(x):
        return (2**x) - 1

    for n in h.values(): 
        res *= formula(n)

    return res

# Example usage
test_arr = [1, 2, 3, 4]
result = countSubarraysWithDistinctValues(test_arr)
print(result)
   
# Example usage
test_arr = [1, 2, 2, 3, 3, 4]
result = countSubarraysWithDistinctValues(test_arr)
print("Number of subarrays with the same total distinct values:", result)

test_arr = [1, 2, 2, 4]
result = countSubarraysWithDistinctValues(test_arr)
print("Number of subarrays with the same total distinct values:", result)

test_arr = [1, 2, 2, 3, 3, 3, 4]
result = countSubarraysWithDistinctValues(test_arr)
print("Number of subarrays with the same total distinct values:", result)



# def generateSubarrays(arr):
#     subarrays = []
#     n = len(arr)
#     for i in range(n):
#         for j in range(i, n):
#             subarrays.append(arr[i:j+1])

#     return subarrays

# # Example usage
# test_arr = [1, 2, 3, 4]
# result = generateSubarrays(test_arr)
# print("All subarrays:", result)