# 1249. Minimum Remove to Make Valid Parentheses
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = list(s)
        stack = [] # remainder will be index to remove 

        for i in range(len(st)):
            if st[i] == '(':
                stack.append(i)
            
            if st[i] == ')':
                if stack: 
                    stack.pop() # () matched, so no need to remove from st
                else:
                    st[i] = '' # nothing to cancel so set to ''
            
        # if there is still ( index in the stack, remove them in st
        while stack:
            idx = stack.pop()
            st[idx] = ''

        return ''.join(st)             
