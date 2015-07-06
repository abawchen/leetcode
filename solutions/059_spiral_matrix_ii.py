# Given an integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

# For example,
# Given n = 3,
# You should return the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        
        matrix = [[0 for x in range(n)] for x in range(n)]

        boundaries = [n-1, n-1, 0, 1] #r, d, l, u
        bi = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] #r, d, l, u
        di = 0
        e = [0, 0]
        ei = 1
        for i in xrange(n*n):
            matrix[e[0]][e[1]] = i+1
            if e[ei] == boundaries[bi]:
                boundaries[bi] -= directions[di][ei]
                bi = (bi+1)%4
                di = (di+1)%4
                ei = (ei+1)%2

            e[0] += directions[di][0]
            e[1] += directions[di][1]

        return matrix

