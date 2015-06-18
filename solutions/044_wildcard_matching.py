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
        return self._recursiveMatch(s, p)

    def _recursiveMatch(self, s, p):
        # print "here:", (s, p)
        if not s:
            sp = set(p)
            if len(sp) == 1 and sp.pop() == '*':
                return True

        i = j = 0
        while j < len(p) and i < len(s):
            if p[j] == '?' or s[i] == p[j]:
                i, j = i+1, j+1
            elif p[j] == '*':
                m, c = j+1, 0
                while m < len(p) and p[m] in ('*', '?'):
                    if p[m] == '?':
                        c += 1
                    m += 1

                if m == len(p):
                    return True

                # idx = s.rfind(p[m])
                # while idx != -1:
                #     if self._recursiveMatch(s[idx+1:], p[m+1:]):
                #         return True
                #     idx = s[:idx].rfind(p[m])

                # idx = s.find(p[m])
                # pos = idx+1
                # while idx != -1:
                #     if self._recursiveMatch(s[pos:], p[m+1:]):
                #         return True
                #     idx = s[pos:].find(p[m])
                #     pos += idx+1

                return False
            else:
                return False

        return i == len(s) and j == len(p)
