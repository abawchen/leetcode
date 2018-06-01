class Solution(object):

    def isUgly(self, num):
        if num <= 0:
            return False

        return self._isUgly(num)

    def _isUgly(self, num):
        if num <= 3:
            return True

        for u in [2, 3, 5]:
            if num % u == 0:
                return self._isUgly(int(num/u))

        return False
