# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# For example,
# Given s = "Hello World",
# return 5. 

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):

        if not s:
            return 0

        count = 0
        start = end = -1
        for i, c in enumerate(s):
            if c == ' ':
                if start != -1:
                    count = end - start + 1
                    start = end = -1
            else:
                if start == -1:
                    start = i
                end = i

        if s[-1] != ' ':
            count = len(s) - start

        return count