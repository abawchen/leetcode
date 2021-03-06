# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

# click to show follow up.
# Follow up:

# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        fr = fc = False
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
                    if i == 0:
                        fr = True
                    if j == 0:
                        fc = True

        for j in xrange(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in xrange(1, len(matrix)):
                    matrix[i][j] = 0

        for i in xrange(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in xrange(1, len(matrix[0])):
                    matrix[i][j] = 0

        if fr:
            for j in xrange(len(matrix[0])):
                matrix[0][j] = 0
        if fc:
            for i in xrange(len(matrix)):
                matrix[i][0] = 0

        # for test
        # return matrix