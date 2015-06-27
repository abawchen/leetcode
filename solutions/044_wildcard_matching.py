# -*- coding: utf-8 -*-
# Implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if p:
            p = self._simplifyPattern(p, p[0], p[0])

        if not s:
            return p == '*' or not p

        if not p:
            return not s

        # print "len(p):", len(p)
        dp = [0] * len(s)

        if p[0] == '*':
            dp = [1] * len(s)
        elif p[0] == '?':
            dp[0] = 1
        else:
            if p[0] != s[0]:
                return False
            dp[0] = 1

        i, j, pre = 0, 1, p[0]
        while j < len(p):
            if p[j] == '*':
                for k in range(i, len(s)):
                    dp[k] = j+1
            elif p[j] == '?':
                if pre != '*':
                    for k in range(i, len(s)-1):
                        if dp[k] == j:
                            dp[k+1] = j+1
                else:
                    for k in range(i, len(s)):
                        dp[k] = j+1
                i += 1
            else:
                offset = 0 if pre == '*' else 1
                first = False
                cdp = dp[:]
                for k in range(i, len(s)):
                    if cdp[k-offset] == j and s[k] == p[j]:
                        dp[k] = j+1
                        i, first = k if not first else i, True
                if not first:
                    break

            j, pre = j+1, p[j]

        return dp[-1] == len(p)


    def _simplifyPattern(self, p, sp, pre):

        for c in p[1:]:
            if c == '*' and pre == '*':
                continue
            
            sp, pre = sp+c, c

        return sp

    # def _cutTail(self, s, p):
    #     i, j = len(s)-1, len(p)-1
    #     while i >= 0 and j >= 0 and p[j] != '*':
    #         if p[j] != '?' and p[i] != p[j]:
    #             return -1, -1
    #         i, i = i-1, j-1
    #     return s[:i], p[:j]

    # def _isMatch(self, s, p):
    #     # print "here:", (s, p)
    #     if not s:
    #         sp = set(p)
    #         if len(sp) == 1 and sp.pop() == '*':
    #             return True

    #     i = j = 0
    #     while i < len(s) and j < len(p):
    #         # print (i, j), (s[i], p[j])
    #         if p[j] == '?' or s[i] == p[j]:
    #             i, j = i+1, j+1
    #             continue
    #         elif p[j] == '*':
    #             m, c = j+1, 0
    #             while m < len(p) and p[m] in ('*', '?'):
    #                 if p[m] == '?':
    #                     c += 1
    #                 m += 1

    #             if m == len(p):
    #                 return True

    #             # longest
    #             idx = s.rfind(p[m])
    #             while idx != -1:
    #                 if self._isMatch(s[idx+1:], p[m+1:]):
    #                     return True
    #                 idx = s[:idx].rfind(p[m])

    #             return False
                
    #             # shortest
    #             # idx = s.find(p[m])
    #             # pos = idx+1
    #             # while idx != -1:
    #             #     if self._isMatch(s[pos:], p[m+1:]):
    #             #         return True
    #             #     idx = s[pos:].find(p[m])
    #             #     pos += idx+1
    #             # return False
            
    #         return False

    #     return i == len(s) and j == len(p)
