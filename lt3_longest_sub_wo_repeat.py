# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Input: s = ""tmmzuxt""
# Output: 5
# Explanation: The answer is "b", with the length of 1.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        if s == "":
            return 0

        seen = {s[0]: 0}
        left = 0 
        res = 1
        for right in range(1, len(s)):
            if s[right] not in seen or seen[s[right]]<left: 
                # OR is used because "tmmzuxt" t match t but left = 2
                seen[s[right]]=right
                right += 1
                res = max(res, len(s[left:right]))
            else: 
                # abcab then start from c 
                left = seen[s[right]]+1
                seen[s[right]] = right
                right = left+1

        return res