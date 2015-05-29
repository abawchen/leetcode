# Given a string S, find the longest palindromic substring in S.
# You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if not s:
            return s

        answer = ""
        longest = 1
        step = -1
        starts = []
        start = mid = len(s)/2 if len(s)%2 == 1 else len(s)/2 - 1
        while start < len(s):
            if start >=0:
                starts.append(start)
            start += step
            step = -step+1 if step < 0 else -step-1

        for start in starts:

            if start <= mid:
                check = (start + 1) * 2 > longest
            else:
                check = (len(s) - start) * 2 > longest
                if not check:
                    break

            if check:
                # odd
                left, right = start-1, start+1
                length, result = self.extendString(s, left, right)
                if length + 1 > longest:
                    longest = length + 1
                    answer = result

                # even
                length, result = self.extendString(s, start, start+1)
                if length > longest:
                    longest = length
                    answer = result

        return s[0] if longest == 1 else answer



    def extendString(self, s, left, right):
        length = 0
        answer = ""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            answer = s[left:right+1]
            length += 2
            left -= 1
            right += 1

        return length, answer


s = Solution()
print s.longestPalindrome(None)
# print s.longestPalindrome("")
# print s.longestPalindrome("1")
# print s.longestPalindrome("11")
# print s.longestPalindrome("abcba")
# print s.longestPalindrome("abccba")
# print s.longestPalindrome("forgeeksskeegfor")
# print s.longestPalindrome("forgeeksskeegfoqq")

print s.longestPalindrome("banana")