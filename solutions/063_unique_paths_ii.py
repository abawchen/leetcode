# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,

# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]

# The total number of unique paths is 2.

# Note: m and n will be at most 100.


class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not len(obstacleGrid) or not len(obstacleGrid[0]) or obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        paths = [ [0 for x in range(n)] for x in range(m)]
        paths[0][0] = 1
        
        for i in range(1, m):
            paths[i][0] = 1 if not obstacleGrid[i][0] and paths[i-1][0] else 0

        for j in range(1, n):
            paths[0][j] = 1 if not obstacleGrid[0][j] and paths[0][j-1] else 0

        print paths
        
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1] if not obstacleGrid[i][j] else 0

        return paths[-1][-1]