# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4. 


class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        stack = []
        longest = val = 0

        for c in s:
            if c == '(':
                stack.append(('(', val))
                val = 0
            else:
                if stack:
                    _, acu = stack.pop()
                    val += acu + 1
                    longest = max(longest, val)
                else:
                    val = 0

        return longest * 2