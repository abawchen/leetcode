class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return float(1)

        self.dic = {1:x}
        result = self._calculate(abs(n))

        return float(result) if n > 0 else 1.0/result

    
    def _calculate(self, n):
        if n == 1:
            return self.dic[1]
        else:
            self.dic[n] = self._calculate(n/2) * self.dic[n/2] * (self.dic[1] if n%2 else 1)
            return self.dic[n]


s = Solution()
print s.myPow(2, 0)
print s.myPow(2, 1)
print s.myPow(2, 2)
print s.myPow(2, 3)
print s.myPow(2, 4)
print s.myPow(2, 6)
print s.myPow(2, 7)
print s.myPow(2, 8)
# print s.myPow(2, 10)
# print s.myPow(2, -8)
print s.myPow(2.3, -8)