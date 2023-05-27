#%%
#recursion 

def fib(n):
    if n <= 1:
        return n 
    
    return fib(n-1) +fib(n-2)

#test case 
print(fib(6))

#memoization
def fib_memo(n):
    memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

#test case
print(fib_memo(6))
# %%
