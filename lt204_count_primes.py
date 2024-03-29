# Given an integer n, return the number of prime numbers that are strictly less than n.


# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        #option 1 easy to understand
        if n <= 2: 
            return 0 
        
        primes = [True] * n 
        primes[0] = primes[1] = False # 1, 2 is not prime

        for num in range(2, n):
            if primes[num]: # some numbers are marked in the following for loop
                # not prime: start with 2* number every n*number is not prime
                for not_prime in range(2*num, n, num):
                    primes[not_prime] = False

        #finally, those not marked False are prime, True = 1
        return sum(primes) 

        # # brute force with memoization
        # prime = set()
        # res = 0
        # def is_prime(num, prime):
        #     if num in prime: # no need to calculate again
        #         return True
        #     if num > 3: 
        #         # print(list(range(2, round((num**0.5))+1)))
        #         for i in range(2, round((num**0.5))+1):
        #             if num % i == 0: 
        #                 return False
        #     return True

        # for ele in range(2, n): 
        #     if is_prime(ele, prime):
        #         res += 1
        
        # return res





        #Option3: Sieve of Eratosthenes
        # We are only interested in numbers LESS than the input number
        # exit early for numbers LESS than 2; (two is prime)
        if n < 2:
            return 0
        
        # create strike list for the input range, initializing all indices to
        # prime (1).
        strikes = [1] * n

        # we know that 0 and 2 are not prime
        strikes[0] = 0
        strikes[1] = 0
        
        # Now set multiples of remaining numbers that are marked as prime to
        # not prime.  It is safe ignore numbers alreay marked as not prime
        # because there are factor(s) that divide evenly into this number and
        # all its multiples.  Use upper limit of (n**0.5)+1, because:
        #  (a) the smallest factor of a non-prime number will not be > sqrt(n).
        #      Ex. non-prime = 100, 
        #           5*20
        #           10*10, 
        #           20*5   # !! we have seen 5 before.
        for i in range(2, int(n**0.5)+1):
            if  strikes[i] != 0:
                # slow:
                #for j in range(i*i, n, i):
                #    strikes[j] = 0

                # 3x faster:
                # strikes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)
                # n = 11
                # i = 2
                # (n-1-i*i)//i + 1
                # (n-1)               # get total # of indicies for n (non-inclusive)
                #     -i*i            # shift to get # of slots in range of interest
                #          //i        # get number of groups
                #              + 1    # get number of slots
                # strikes[2*2:11:2]  = [0] * ((11-1-2*2)//2 + 1
                # strikes[4:11:2]    = [0] * 4
                # s[4], s[6], s[8], s10] = 0, 0, 0, 0
                strikes[i*i:n:i] = [0] * ((n-1-i*i)//i + 1)

        return sum(strikes)