# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # use adjacency graph, check if there is cycle in directed graph 
        #if there is 1 pair then True
        if len(prerequisites) <= 1: return True
        graph = {i: [] for i in range(numCourses)}
        for x, y in prerequisites: 
            graph[x].append(y)

        visited = set()

        def dfs(course):
            #base case 1: if course is revisited then cycle
            if course in visited:
                return False 
            #base case 2: if course has no prerequisit then good
            if graph[course] == []: 
                return True
            visited.add(course)
            #for each connected course, check to the end 
            for pre in graph[course]:
                if not dfs(pre): # as long as there is cycle 
                    return False 
            
            # all other cases return true 
            # optimization: remove prerequisit after verifying a course 
            graph[course] = []
            #$$$ important because we are going course by course to check if cycle
            visited.remove(course)
            return True 
        
        # for each course in the graph, run dfs, in case the graph are separated 
        #eg: [[1,2], [3,4]]
        for x in range(numCourses):
            if not dfs(x): 
                return False 
        return True 
        


