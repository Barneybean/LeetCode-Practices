# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if s == '': return []

        h = set()
        res = set()

        #for loop - faster
        for i in range(9,len(s)):
            target = s[i-9: i+1]
            if target not in h: 
                h.add(target)
            else:
                res.add(target)
        return res


        #two pointers
        # l, r = 0, 10
        # while r <= len(s):
        #     target = s[l:r]
        #     print(target)
        #     if target not in h: 
        #         h.add(target)
        #     else:
        #         res.add(target)
        #     l += 1
        #     r += 1
        # return res

