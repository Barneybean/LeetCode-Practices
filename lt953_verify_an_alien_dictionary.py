# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# # 

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # check if word in words is sorted: "word","world" is not sorted becuase according to the 4th position, l is < d according to alien dict so "world","word" is right 
        
        #####  idea, Translate alien words to normal earth order, if the translation is sorted then alien word is also sorted 

        # "world" is in alien order "worldabcefghijkmnpqstuvxyz"
        # normal alp = 'abcdefghijklmnopqrstuvwxyz'
        # the translation is {alien: earth}
        # {'h': 'a', 'l': 'b', 'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'h', 'g': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}

        alp = 'abcdefghijklmnopqrstuvwxyz'
        d = {}
        for i in range(len(order)):
            d[order[i]] = alp[i]
        print(d)

        def translate(word):
            earth_lan = ''
            for w in word:
                earth_lan += d[w]
            return earth_lan

        for i in range(len(words)-1):
            if translate(words[i]) > translate(words[i+1]):
                return False
        
        return True


        # # Option 2: turn alien words into numbers  will timeout 
        # d = {ch: str(n+1) for n, ch in enumerate(order)} # start with 1 to avoid 0 in first letter 
        # print(d)
        # # {'n': '0', 'g': '1', 'x': '2', 'l': '3', 'k': '4', 't': '5', 'h': '6', 's': '7', 'j': '8', 'u': '9', 'o': '10', 'q': '11', 'c': '12', 'p': '13', 'a': '14', 'v': '15', 'b': '16', 'f': '17', 'd': '18', 'e': '19', 'r': '20', 'm': '21', 'i': '22', 'y': '23', 'w': '24', 'z': '25'}
        # # ["kuvp","q"] need to compare k and q 
        # if len(words) == 1: return True

        # def convert_word(word):
        #     num = ''
        #     for s in word:
        #         num += d[s]
        #     return num

        # for i in range(len(words)-1):
        #     num1 = convert_word(words[i])
        #     num2 = convert_word(words[i+1])
        #     # compare from left 
        #     a, b = 0, 0 
        #     while a < len(num1) and b < len(num2):
        #         if num1[a]>num2[b]:
        #             return False
        
        # return True


        
        