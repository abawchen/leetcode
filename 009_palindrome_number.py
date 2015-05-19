class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            return self._isPalindromeString(str(x))

    def _isPalindromeString(self, s):
        if s[0] != s[-1]:
            return False
        else:
            return True if len(s[1:-1]) <= 1 else self._isPalindromeString(s[1:-1])

s = Solution()
print s.isPalindrome(9)
print s.isPalindrome(99)
print s.isPalindrome(121)
print s.isPalindrome(123) # False
print s.isPalindrome(1221)
print s.isPalindrome(12321)
print s.isPalindrome(1000021)
