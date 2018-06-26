class Solution:

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        from math import sqrt
        self.sqrt = sqrt
        self.m = n+1
        self.ans = [self.m] * (n+1)
        self.ans[0] = 0
        for i in range(1, int(self.sqrt(n))+1):
            self.ans[i*i] = 1
        self._numSquares(n, 1)
        return self.ans[n]


    def _numSquares(self, left, level):
        while self.ans[left] == self.m:
            root = int(self.sqrt(left))
            for r in range(root, 0, -1):
                n = left-r*r
                if self.ans[left] == self.m:
                    self.ans[left] = 1+self._numSquares(n, level+1)
                elif self.ans[n] != self.m:
                    self.ans[left] = min(self.ans[left], 1+self.ans[n])
                elif level+1 < self.ans[left]:
                    self.ans[left] = min(self.ans[left], 1+self._numSquares(n, level+1))
        return self.ans[left]
