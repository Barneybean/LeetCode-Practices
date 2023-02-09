# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.


# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

class Solution:
    def counter(self, s: str) -> dict:
        f = {}
        for e in s:
            f[e] = s.count(e)
        return f 

    def minWindow(self, s: str, t: str) -> str:
        # use dict of char count to keep track of the number of char found 
        # two pointer: move right until 1st res found, then move left to find the least lenght for the 1st res
        # remove the first char in the res and continue to move right to find new res 
        # compare the new res with existing res for the least 
        if s == t or t == '': 
            return t
        counter_t = self.counter(t) 
        # can be replaced with collections.counter()
        left = 0 
        queue = [] # to move start point to next char in t for next possible res
        tmp = ""
        res = ""
        for right in range(len(s)):
            if s[right] in counter_t:
                # eliminate char if included in substring
                queue.append(right)
                counter_t[s[right]] -= 1 
                right += 1 
                tmp = s[left : right]
                if max(list(counter_t.values())) <= 0: # res found 
                    if len(tmp)<len(res) or res == "": 
                        res = tmp
                    # remove 1 first qualified char and continue finding next res 
                    idx = queue.pop(0)
                    counter_t[s[idx]]+=1 
                    if queue:
                        left = queue[0]
                    tmp = s[left : right]   
                    # keep shrinking until only 1 char is missing, then move right pointer to next eg: s = "acbbaca" t = 'aba' => acbba is 1st res then move to 'ba' and find next a
                    while counter_t[s[left]] < 0 and res!= '': 
                        idx = queue.pop(0)
                        counter_t[s[idx]]+=1 
                        left = queue[0]  
                        tmp = s[left : right] 
                    if max(list(counter_t.values()))<=0 and len(tmp)<len(res):
                        res = tmp
            else:
                right += 1 
                if not queue:
                    # eg: s = 'ab' t = 'b'
                    left += 1

        return res




