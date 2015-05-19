class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        flip = x < 0
        s = self._reverseString(str(abs(x)))

        return 0 if int(s) >= pow(2, 31) else (int(s) * (-1 if flip else 1))

    def _reverseString(self, s):
        if len(s) == 1:
            return s

        return self._reverseString(s[1:]) + s[0]


s = Solution()
print s.reverse(103)  # 301
print s.reverse(-103) # -301

print s.reverse(1000000003)
print s.reverse(1563847412)

# 2147483651
# 2147483648

print s.reverse(1)  # 301

# 3000000001
# 4294967296
# 4294967295


# 0
# 1  => 2

# 00
# 11 => 3