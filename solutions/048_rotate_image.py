# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Follow up:
# Could you do this in-place?


class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        if not matrix:
            return

        m, n = 0, len(matrix)
        for i in xrange(n, 0, -2):
            for ps in self.calPairs(i, m):
                self.swap(matrix, ps)
            m += 1

        # return matrix #for test
    
    def calPairs(self, n, m):
        l = []
        for i in xrange(n-1):
            l.append([(x+m, y+m) for (x, y) in [(0, i), (i, n-1), (n-1, n-1-i), (n-1-i, 0)]])
        return l

    def swap(self, mx, ps):
        mx[ps[0][0]][ps[0][1]], mx[ps[1][0]][ps[1][1]], mx[ps[2][0]][ps[2][1]], mx[ps[3][0]][ps[3][1]] = mx[ps[3][0]][ps[3][1]], mx[ps[0][0]][ps[0][1]], mx[ps[1][0]][ps[1][1]], mx[ps[2][0]][ps[2][1]]