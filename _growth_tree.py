# [* H * * * ]
# [H * * * * ]
# [ * * * * H]
# [ * * H * *]

# 2D matrix, H stands for house, * stands for empty spots and these empty spots can be planted with trees
# Find the minium number of trees need to be planted and they will be neighbouring to each house, and the neighbouring condition is 8 directions neighbored

# the answer should be ( t stands for trees)
# [* H * * * ]
# [H t * * * ]
# [ * * * t H]
# [ * * H * *]

matrix = [
    ['*', 'H', '*', '*', '*'],
    ['H', '*', '*', '*', '*'],
    ['*', '*', '*', '*', 'H'],
    ['*', '*', 'H', '*', '*'],
]

def unvisited_houses(matrix, row, column, visited):
    result = set()
    for dr, dc in (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1):
        r = row + dr
        c = column + dc
        if r < 0 or r >= len(matrix):
            continue
        if c < 0 or c >= len(matrix[r]):
            continue
        if matrix[r][c] == 'H' and (r, c) not in visited:
            result.add((r, c))
    return result

min_trees = float('inf')
min_trees_matrix = None

def backtrack(matrix, row, column, houses, trees, visited):
    global min_trees, min_trees_matrix
    if houses == 0:
        if trees < min_trees:
            min_trees = trees
            min_trees_matrix = [row[:] for row in matrix]
        return
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] != '*':
                continue
            u = unvisited_houses(matrix, row, column, visited)
            if len(u) == 0:
                continue
            matrix[row][column] = 't'
            backtrack(matrix, row, column, houses - len(u), trees + 1, visited | u)
            matrix[row][column] = '*'

houses = 0
for row in range(len(matrix)):
    for column in range(len(matrix[row])):
        if matrix[row][column] == 'H':
            houses += 1

backtrack(matrix, 0, 0, houses, 0, set())

print(min_trees) # 2
for row in min_trees_matrix:
    print(row)

# ['t', 'H', '*', '*', '*']
# ['H', '*', '*', '*', '*']
# ['*', '*', '*', 't', 'H']
# ['*', '*', 'H', '*', '*']