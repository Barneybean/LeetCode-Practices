# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

# Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

# You may assume that the borders of the maze are all walls (see examples).

 

# Example 1:


# Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
# Example 2:


# Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
# Output: false
# Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.
# Example 3:

# Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
# Output: false

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not start or not destination:
            # bad input
            return False
        if start == destination:
            # input start and destination were the same
            return True

        q = deque([(start[0], start[1])])
        # using a deque is important when used as a queue
        # stack here would be DFS
        visited = set()
        # a set will provide constant time access, we will never have duplicates
        directions_to_go = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # we can always roll north, south, east, or west

        while q:
            current = q.popleft()
            # first in first out (swap to pop here with stack for DFS)
            if current[0] == destination[0] and current[1] == destination[1]:
                return True
            for direction in directions_to_go:
                # move in a direction
                r, c = current[0], current[1]
                new_r = r + direction[0]
                new_c = c + direction[1]
                while 0 <= new_r < len(maze) and 0 <= new_c < len(maze[0]) and maze[new_r][new_c] == 0:
                    # keep moving until ONE PAST where you can't move (roll) anymore
                    new_r += direction[0]
                    new_c += direction[1]
                # roll back one so that you're actually where you should be
                rolled_to_x = new_r - direction[0]
                rolled_to_y = new_c - direction[1]
                if (rolled_to_x, rolled_to_y) not in visited:
                    visited.add((rolled_to_x, rolled_to_y))
                    # add this position to be searched from as well
                    q.append((rolled_to_x, rolled_to_y))
        # if you're here no solution was found and everything has been visited
        return False
        # this solution keeps the ball rolling untill hitting the wall or hit the target then use this as a next start in the queue to contnue

        