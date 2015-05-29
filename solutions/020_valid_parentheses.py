# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):

        stack = []
        pairs = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in pairs:
                stack.append(c)
            elif stack:
                if pairs[stack.pop()] != c:
                    return False
            else:
                return False

        return not stack


s = Solution()

print s.isValid("()")
print s.isValid("()[]{}")
print s.isValid("(]")
print s.isValid("([)]")
print s.isValid("{[()]}")
print s.isValid("[{[()]}]]]")
print s.isValid("({})[[][]]")

print s.isValid("")