# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.


# Example 1:

# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# Example 2:

# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        #Option 1: less efficient way 
        # bull = 0 
        # cow = 0
        # copy_secret = [x for x in secret]
        # copy_guess = [x for x in guess]

        # for i in range(len(guess)):
        #     # if guess[i] not in guess: # duplication [2,2,1,3], 2 will only count once
        #     if guess[i] == secret[i]:
        #         bull += 1
        #         copy_secret.remove(secret[i])
        #         copy_guess.remove(guess[i])
            
        # for j in range(len(copy_guess)):
        #     if copy_guess[j] in copy_secret:
        #         cow += 1
        #         copy_secret.remove(copy_guess[j])
        #     # print(copy)
        # return f"{bull}A{cow}B"

        #Option 2 use hashmap faster 
        a = {}
        b = {}
        cow = 0
        bull = 0
        
        for i in secret: 
            a[i] = a.get(i, 0) + 1
        
        for j in guess: 
            b[j] = b.get(j, 0) + 1
        
        for i in range(len(guess)):
            # if guess[i] not in guess: # duplication [2,2,1,3], 2 will only count once
            if guess[i] == secret[i]:
                bull += 1
                a[secret[i]] -= 1
                b[guess[i]] -= 1

        for k in a: # for each key in a
            if k in b: # if there is a match
                cow += min(a[k], b[k])
    
        return f"{bull}A{cow}B"



