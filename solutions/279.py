class Solution:
    from math import sqrt

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = n
        while left != 0:
            int root = sqrt(left)
            left = left - root*root


    def _numSquares(self, n):
