# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]

# You should return [1,2,3,6,9,8,7,4,5]. 


class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):

        if not matrix or not matrix[0]:
            return []

        total = len(matrix) * len(matrix[0])
        spiral = []

        l, r, u, d = -1, len(matrix[0]), 0, len(matrix)
        s, i, j = 0, 0, 0

        for c in range(total):
            spiral.append(matrix[i][j])
            s, i, j, l, r, u, d = self._next(s, i, j, l, r, u, d)

        return spiral


    def _next(self, s, i, j, l, r, u, d):
            if s == 0: # step right
                j += 1
                if j == r:
                    i, j = i+1, r-1
                    r -= 1
                    s = 1
            elif s == 1: # step down
                i += 1
                if i == d:
                    i, j = d-1, j-1
                    d -= 1
                    s = 2
            elif s == 2: # step left
                j -= 1
                if j == l:
                    i, j = i-1, l+1
                    l += 1
                    s = 3
            else: # step up
                i -= 1
                if i == u:
                    i, j = u+1, j+1
                    u += 1
                    s = 0

            return s, i, j, l, r, u, d