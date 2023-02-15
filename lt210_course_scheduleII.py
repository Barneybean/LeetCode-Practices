"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:  
        # oputput is the order of courses to take, if not possible then return []

        graph = {i:[] for i in range(numCourses)}
        for x, y in prerequisites: 
            graph[x].append(y)

        visited = set()
        processed = set()
        output = []

        def dfs(course):
            if course in visited:
                return False 
            if course in processed:
                return True 
            
            visited.add(course)
            
            for c in graph[course]:
                # if in visited, there is cycle. not Fasle = True
                if dfs(c) == False: return False 
            
            visited.remove(course) ###
            processed.add(course)
            output.append(course) ### going by the order of visit
            return True
        
        for i in range(numCourses):
            if not dfs(i): # as long as there is cycle then []
                return [] 
        return output
                

        