# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 
class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci: start from end stair
        # 1, 2, 3, 4, 5 stairs 
        # 5 to 5 has 1 option,
        # 4 to 5 has 1 option 
        # 3 to 5 has 1+1 = 2 options 
        # 2 to 5 has 1+2 = 3 options 
        # 1 to 5 has 2+3 = 5 options: 1 jump to 2 or 3, and 2 to 5 has 3 options, 3 to 5 has 2 options
        # use two pointers

        one, two = 1, 1 # one = 4th, two = 5th stair in the example
        # new one = 3rd stair and new two = 4th  
        for i in range(n-1):
            temp = one 
            one = one + two 
            two = temp # old 1 
        
        return one 