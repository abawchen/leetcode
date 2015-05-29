class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if s == None:
            return 0

        dic = {}
        local = 0
        length = 0
        clear = 0
        for i in xrange(0, len(s)):
            j = i
            c = s[i]
            if dic.has_key(c):
                length = max(length, local)
                local = i - dic[c]
                i = dic[c] + 1
                for m in xrange(clear, dic[c]):
                    dic.pop(s[m], None)
                clear = i
            else:
                local += 1
            dic[c] = j

        return max(length, local)


s = Solution()
print(s.lengthOfLongestSubstring(None))
print(s.lengthOfLongestSubstring(""))
print(s.lengthOfLongestSubstring("a"))
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("ABDEFGABEF"))
print(s.lengthOfLongestSubstring("GEEKSFORGEEKS"))
print(s.lengthOfLongestSubstring("abcabcd"))