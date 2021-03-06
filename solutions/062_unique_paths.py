# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# Above is a 3 x 7 grid. How many possible unique paths are there?

# Note: m and n will be at most 100.

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        # (x+y)!/x!y!

        if m == 0 or n == 0:
            return 0

        paths = [[1 for x in range(n)] for x in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

        return paths[-1][-1]
