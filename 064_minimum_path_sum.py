import time

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return

        dic = {(0, 0): grid[0][0]}
        
        rows = len(grid)
        columns = len(grid[0])
        for i in xrange(1, rows):
            dic[(i, 0)] = dic[(i-1, 0)] + grid[i][0]

        for j in xrange(1, columns):
            dic[(0, j)] = dic[(0, j-1)] + grid[0][j]

        for i in xrange(1, rows):
            for j in xrange(1, columns):
                dic[(i, j)] = grid[i][j] + min(dic[(i-1, j)], dic[(i, j-1)])

        return dic[(rows-1, columns-1)]

s = Solution()

# grid = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
# print(s.minPathSum(grid))
# # 3


# grid = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
# print(s.minPathSum(grid))


# grid = [[1], [1], [5]]
# print(s.minPathSum(grid))

# grid = [[1, 1, 5]]
# print(s.minPathSum(grid))

# grid = [[1]]
# print(s.minPathSum(grid))

# print(s.minPathSum([]))
# print(s.minPathSum([[]]))
# print(s.minPathSum(None))


print(s.minPathSum([[1,2],[1,1]]))
