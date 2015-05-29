# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000

# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011

# Answer: 3

def numIslands(grid):
    num = 0
    isEmpty = len(grid) == 0 or len(grid[0]) == 0
    if isEmpty:
        return num

    dic = {}
    rows = len(grid)
    columns = len(grid[0])
    islandKey = lambda x, y: str(x) + ',' + str(y)
    stepable = lambda x, y: x >= 0 and x < rows and y >= 0 and y < columns and grid[x][y] == '1' and not dic.has_key(islandKey(x, y))

    for x in xrange(rows):
        for y in xrange(columns):
            if grid[x][y] == '1':
                key = islandKey(x, y)
                if not dic.has_key(key):
                    num += 1
                    dic[key] = num
                    stack = [(x, y)]
                    while len(stack) > 0:
                        m, n = stack.pop()
                        # up
                        if stepable(m-1, n):
                            dic[islandKey(m-1, n)] = num
                            stack.append((m-1, n));
                        
                        # down
                        if stepable(m+1, n):
                            dic[islandKey(m+1, n)] = num
                            stack.append((m+1, n))

                        # left
                        if stepable(m, n-1):
                            dic[islandKey(m, n-1)] = num
                            stack.append((m, n-1))

                        # right
                        if stepable(m, n+1):
                            dic[islandKey(m, n+1)] = num
                            stack.append((m, n+1))

    return num
