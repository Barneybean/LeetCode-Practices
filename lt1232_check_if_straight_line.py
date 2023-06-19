# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        x0,y0=coordinates[0]
        x1,y1=coordinates[1]

        for x, y in coordinates[2:]:
            # remember this formula
            if (y1 - y0)*(x - x0) != (y - y0) * (x1 - x0):
                return False 

        return True
        
        
        
        # # my solution: 
        # if not coordinates or len(coordinates) == 1: 
        #     return False 
        # if len(coordinates) == 2:
        #     return True

        # x0, y0 = coordinates[0]
        # x1, y1 = coordinates[1]
        # is_verticle = False
        # first_slope = 0
        # # if verticle
        # if x1-x0 == 0: 
        #     is_verticle = True
        # else:
        #     # calculate slope 
        #     first_slope = (y1-y0) / (x1-x0)
        
        # for i in range(1, len(coordinates)-1):
        #     if is_verticle: 
        #         if (coordinates[i+1][0] - coordinates[i][0]) != 0:
        #             return False
        #         continue # no need to check slope because it should be verticle and no slope
            
        #     #non verticle
        #     if (coordinates[i+1][0] - coordinates[i][0]) == 0:
        #         return False
        #     else:
        #         slope = (coordinates[i+1][1] - coordinates[i][1]) / (coordinates[i+1][0] - coordinates[i][0])
        #         if slope != first_slope:
        #             return False 
        
        # return True
                
