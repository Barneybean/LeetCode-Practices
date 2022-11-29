# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
  
def isValid(s: str) -> bool:
        pair = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        if len(s)<2: 
            return False
        if s[0] not in pair:
            return False

        stack = [s[0]]
        for e in s[1:]: 
            # print(e, 'stack', stack)
            if e in pair:
                stack.append(e) # add if it is beginning of the pair
            else:
                if not stack: # if the stack is empty means nothing to cancel
                    return False 
                # print(e)
                last = stack.pop() # check if the next can cancel the first
                if e == pair[last]:
                    pass
                else:
                    return False
        # after for loop, the stack should be empty to return True
        if stack:
            return False
        else:
            return True

