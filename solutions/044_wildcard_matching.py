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

        if not p:
            return not s

        m, n = len(s), len(p)
        i = j = 0

        # lastS: last matching position of string s
        # lastP: last matching '*' position of pattern p
        lastS = 0
        lastP = -1

        while i < m:
            if j < n and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                lastS = i
                lastP = j
                j += 1
            elif lastP >= 0:
                # When p[j] is failed to matching current s[i],
                # go back to last matching '*' position.
                i = lastS + 1
                lastS += 1
                j = lastP
            else:
                return False

        if i < m:
            return False

        while j < n and p[j] == '*':
            j += 1

        return j == n