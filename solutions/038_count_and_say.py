# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string. 


class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):

        val = "1"
        for i in range(1, n):
            val = self._interpret(val)

        return val
    
    def _interpret(self, val):

        i = 0
        result = ""
        while i < len(val):
            count = 1
            cur = val[i]
            while i+1 < len(val) and cur == val[i+1]:
                count += 1
                i += 1
            result += str(count) + cur
            i += 1

        return result