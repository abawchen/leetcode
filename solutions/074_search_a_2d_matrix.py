# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.

# For example,

# Consider the following matrix: 
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]

# Given target = 3, return true.

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        
        r = self._searchRow(matrix, target, 0, len(matrix)-1)
        if r == -1:
            return False

        c = self._searchColumn(matrix[r], target, 0, len(matrix[0])-1)
        # print (r, c)
        return c != -1

    def _searchRow(self, matrix, target, lr, ur):
        if lr > ur:
            return -1

        mr = (lr + ur)/2

        if matrix[mr][0] <= target and matrix[mr][-1] >= target:
            return mr

        lr, ur = (lr, mr-1) if target < matrix[mr][0] else (mr+1, ur)
        return self._searchRow(matrix, target, lr, ur)

    def _searchColumn(self, array, target, lc, uc):
        if lc > uc:
            return -1

        mc = (lc + uc)/2

        if array[mc] == target:
            return mc

        lc, uc = (lc, mc-1) if target < array[mc] else (mc+1, uc)
        return self._searchColumn(array, target, lc, uc)