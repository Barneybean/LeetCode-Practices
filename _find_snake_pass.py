'''
We have a two-dimensional board game involving snakes.  The board has two types of squares on it: +'s represent impassable squares where snakes cannot go, and 0's represent squares through which snakes can move.

Snakes may move in any of four directions - up, down, left, or right - one square at a time, but they will never return to a square that they've already visited.  If a snake enters the board on an edge square, we want to catch it at a different exit square on the board's edge.

The snake is familiar with the board and will take the route to the nearest reachable exit, in terms of the number of squares it has to move through to get there. Note that there may not be a reachable exit.

Here is an example board:

    col-->        0  1  2  3  4  5  6  7  8
               +---------------------------
    row      0 |  +  +  +  +  +  +  +  0  0
     |       1 |  +  +  0  0  0  0  0  +  +
     |       2 |  0  0  0  0  0  +  +  0  +
     v       3 |  +  +  0  +  +  +  +  0  0
             4 |  +  +  0  0  0  0  0  0  +
             5 |  +  +  0  +  +  0  +  0  +

Write a function that takes a rectangular board with only +'s and O's, along with a starting point on the edge of the board, and returns the coordinates of the nearest exit to which it can travel.  If there is a tie, return any of the nearest exits.
-----------------------------------------------------
Sample inputs:
board1 = [['+', '+', '+', '+', '+', '+', '+', '0', '0'],
          ['+', '+', '0', '0', '0', '0', '0', '+', '+'],
          ['0', '0', '0', '0', '0', '+', '+', '0', '+'],
          ['+', '+', '0', '+', '+', '+', '+', '0', '0'],
          ['+', '+', '0', '0', '0', '0', '0', '0', '+'],
          ['+', '+', '0', '+', '+', '0', '+', '0', '+']]
start1_1 = (2, 0) # Expected output = (5, 2) 
start1_2 = (0, 7) # Expected output = (0, 8)
start1_3 = (5, 2) # Expected output = (2, 0) or (5, 5)
start1_4 = (5, 5) # Expected output = (5, 7)

board2 = [['+', '+', '+', '+', '+', '+', '+'],
          ['0', '0', '0', '0', '+', '0', '+'],
          ['+', '0', '+', '0', '+', '0', '0'],
          ['+', '0', '0', '0', '+', '+', '+'],
          ['+', '+', '+', '+', '+', '+', '+']]
start2_1 = (1, 0) # Expected output = null (or a special value representing no possible exit)
start2_2 = (2, 6) # Expected output = null 

board3 = [['+', '0', '+', '0', '+',],
          ['0', '0', '+', '0', '0',],
          ['+', '0', '+', '0', '+',],
          ['0', '0', '+', '0', '0',],
          ['+', '0', '+', '0', '+']]
start3_1 = (0, 1) # Expected output = (1, 0)
start3_2 = (4, 1) # Expected output = (3, 0)
start3_3 = (0, 3) # Expected output = (1, 4)
start3_4 = (4, 3) # Expected output = (3, 4)

board4 = [['+', '0', '+', '0', '+',],
          ['0', '0', '0', '0', '0',],
          ['+', '+', '+', '+', '+',],
          ['0', '0', '0', '0', '0',],
          ['+', '0', '+', '0', '+']]
start4_1 = (1, 0) # Expected output = (0, 1)
start4_2 = (1, 4) # Expected output = (0, 3)
start4_3 = (3, 0) # Expected output = (4, 1)
start4_4 = (3, 4) # Expected output = (4, 3)

board5 =  [['+', '0', '0', '0', '+',],
           ['+', '0', '+', '0', '0',],
           ['+', '0', '0', '0', '0',],
           ['+', '0', '0', '0', '+']]
start5_1 = (0, 1) # Expected output = (0, 2)
start5_2 = (3, 1) # Expected output = (3, 2)
start5_3 = (1, 4) # Expected output = (2, 4)

board6 = [['+', '+', '+', '+', '+', '+', '+', '+'],
          ['0', '0', '0', '0', '0', '0', '0', '0'],
          ['+', '0', '0', '0', '0', '0', '0', '0'],
          ['+', '0', '0', '0', '0', '0', '0', '+'],
          ['0', '0', '0', '0', '0', '0', '0', '+'],
          ['+', '+', '+', '+', '+', '+', '0', '+']]

start6_1 = (4,0) # Expected output = (1, 0)

All test cases:
findExit(board1, start1_1) => (5, 2)
findExit(board1, start1_2) => (0, 8)
findExit(board1, start1_3) => (2, 0) or (5, 5)
findExit(board1, start1_4) => (5, 7)
findExit(board2, start2_1) => null (or a special value representing no possible exit)
findExit(board2, start2_2) => null
findExit(board3, start3_1) => (1, 0)
findExit(board3, start3_2) => (3, 0)
findExit(board3, start3_3) => (1, 4)
findExit(board3, start3_4) => (3, 4)
findExit(board4, start4_1) => (0, 1)
findExit(board4, start4_2) => (0, 3)
findExit(board4, start4_3) => (4, 1)
findExit(board4, start4_4) => (4, 3)
findExit(board5, start5_1) => (0, 2)
findExit(board5, start5_2) => (3, 2)
findExit(board5, start5_3) => (2, 4)
findExit(board6, start6_1) => (1, 0)

Complexity Analysis:

r: number of rows in the board
c: number of columns in the board

'''

board1 = [['+', '+', '+', '+', '+', '+', '+', '0', '0'],
           ['+', '+', '0', '0', '0', '0', '0', '+', '+'],
           ['0', '0', '0', '0', '0', '+', '+', '0', '+'],
           ['+', '+', '0', '+', '+', '+', '+', '0', '0'],
           ['+', '+', '0', '0', '0', '0', '0', '0', '+'],
           ['+', '+', '0', '+', '+', '0', '+', '0', '+']]
start1_1 = (2, 0) # Expected output = (5, 2) 
start1_2 = (0, 7) # Expected output = (0, 8)
start1_3 = (5, 2) # Expected output = (2, 0) or (5, 5)
start1_4 = (5, 5) # Expected output = (5, 7)

board2 = [['+', '+', '+', '+', '+', '+', '+'],
           ['0', '0', '0', '0', '+', '0', '+'],
           ['+', '0', '+', '0', '+', '0', '0'],
           ['+', '0', '0', '0', '+', '+', '+'],
           ['+', '+', '+', '+', '+', '+', '+']]
start2_1 = (1, 0) # Expected output = null (or a special value representing no possible exit)
start2_2 = (2, 6) # Expected output = null 

board3 = [['+', '0', '+', '0', '+'],
           ['0', '0', '+', '0', '0'],
           ['+', '0', '+', '0', '+'],
           ['0', '0', '+', '0', '0'],
           ['+', '0', '+', '0', '+']]
start3_1 = (0, 1) # Expected output = (1, 0)
start3_2 = (4, 1) # Expected output = (3, 0)
start3_3 = (0, 3) # Expected output = (1, 4)
start3_4 = (4, 3) # Expected output = (3, 4)

board4 = [['+', '0', '+', '0', '+'],
           ['0', '0', '0', '0', '0'],
           ['+', '+', '+', '+', '+'],
           ['0', '0', '0', '0', '0'],
           ['+', '0', '+', '0', '+']]
start4_1 = (1, 0) # Expected output = (0, 1)
start4_2 = (1, 4) # Expected output = (0, 3)
start4_3 = (3, 0) # Expected output = (4, 1)
start4_4 = (3, 4) # Expected output = (4, 3)

board5 = [['+', '0', '0', '0', '+'],
           ['+', '0', '+', '0', '0'],
           ['+', '0', '0', '0', '0'],
           ['+', '0', '0', '0', '+']]
start5_1 = (0, 1) # Expected output = (0, 2)
start5_2 = (3, 1) # Expected output = (3, 2)
start5_3 = (1, 4) # Expected output = (2, 4)


board6 = [['+', '+', '+', '+', '+', '+', '+', '+'],
          ['0', '0', '0', '0', '0', '0', '0', '0'],
          ['+', '0', '0', '0', '0', '0', '0', '0'],
          ['+', '0', '0', '0', '0', '0', '0', '+'],
          ['0', '0', '0', '0', '0', '0', '0', '+'],
          ['+', '+', '+', '+', '+', '+', '0', '+']]

start6_1 = (4, 0) # Expected output = (1, 0)


def findExit(board, start):
    # alternatively, check snake pass first see if there is straight line to pass, if yes, then output as the shortest 
    if start[1] == 0: 
        # row
        if '+' not in board[start[0]]:
            return (start[0], len(board[0])-1)
    
    if start[0] == 0: 
        if '+' not in [board[x][start[1]] for x in range(len(board))]:
            return (len(board)-1, start[1])

    # given start pos will alwasy be on the edge and 0
    pos = (start[0], start[1])
    
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    
    visited = {start: 0} #start: distance to track distance 
        
    min_distance = float('inf') 
    
    possible_out = None

    # use recursion to find the first output then it should be the shortest

    # better to use queue in BFS, when first output is found then it is the shortest 
    queue = [pos] # start

    while queue: 
        print()
        print('queue', queue)
        cur_pos = queue.pop(0)
        x, y = cur_pos[0], cur_pos[1]
        # bfs using queue 
        for d in directions: 
            new_position = (x+d[0], y+d[1])
            print('new_position', new_position)
            
            # out of index
            if new_position[0] < 0 or new_position[1] < 0 or new_position[0] > len(board)-1 or new_position[1] > len(board[0])-1: # out of index
                print('out of index')
                continue

            # check if hitting +, if yes, do not go 
            if board[new_position[0]][new_position[1]] == '+':
                print('hitting +')
                continue # move to next direction and skip the following codes 
                
            # check if hitting the edge, found an answer, keep finding better answers until all points visited
            # learning, I missed to check the outer boarder, check 0 and len for all boarders !!!!!!!!!!!
            if new_position not in visited and (new_position[0] == 0 or new_position[1] == 0 or new_position[0] == len(board)-1 or new_position[1]== len(board[0])-1):
                print('===============found point out===============')
                # cumulate distance when getting to a unvisited point, add 1 from distance from last point
                visited[new_position] = visited.get(new_position, 1) + visited[pos] 
                new_distance = visited[new_position]
                # print('visited', visited)
                # update the distance if it is a better answer
                if new_distance < min_distance: # found out point that has new min distance 
                    min_distance = new_distance
                    possible_out = new_position 
                
                # continue
                return possible_out
                
            # check if inside the board and still 0: 
            if new_position not in visited and board[new_position[0]][new_position[1]] == '0':
                print('0 and inside board, continue and add to queue')
                visited[new_position] = visited.get(new_position, 1) + visited[pos]
                new_distance = visited[new_position]
                queue.append(new_position) # add new position to queue and use it for next start point 
        # print('new queue', queue)
    return possible_out
            
        
board1 = [['+', '+', '+', '+', '+', '+', '+', '0', '0'],
           ['+', '+', '0', '0', '0', '0', '0', '+', '+'],
           ['0', '0', '0', '0', '0', '+', '+', '0', '+'],
           ['+', '+', '0', '+', '+', '+', '+', '0', '0'],
           ['+', '+', '0', '0', '0', '0', '0', '0', '+'],
           ['+', '+', '0', '+', '+', '0', '+', '0', '+']]
start1_1 = (2, 0) # Expected output = (5, 2) 
start1_2 = (0, 7) # Expected output = (0, 8)
start1_3 = (5, 2) # Expected output = (2, 0) or (5, 5)
start1_4 = (5, 5) # Expected output = (5, 7)
print(findExit(board1, start1_1)) #result (5, 2) pass
print(findExit(board1, start1_2)) #result (0, 8) pass
print(findExit(board1, start1_3)) #result (5, 5) pass
print(findExit(board1, start1_4)) #result (5, 7) pass




# Q1 return row and col index where snake can pass through in straight line
def snake_pass(board):
    res_col = []
    res_row = []
    
    #edge cases
    if board == [[]]: return [res_row, res_col]
    
    # row
    for i in range(len(board)):
        if '+' not in board[i]:
            res_row.append(i)
    
    # col 
    flag = True
    for col_index in range(len(board[0])):
        for row_index in range(len(board)):
            # print(row_index, col_index)
            if board[row_index][col_index] == '+':
                flag = False 
                break
        # print('flag', flag)
        if flag:
            res_col.append(col_index)
        flag = True 

    return [res_row, res_col]
    # board[0][0]
    # board[1][0]
    # board[2][0]
    # n = len(board)

# result = snake_pass(board1)
# print(result)
# result = snake_pass(board2)
# print(result)
# result = snake_pass(board3)
# print(result)
# result = snake_pass(board4)
# print(result)
# result = snake_pass(board5)
# print(result)