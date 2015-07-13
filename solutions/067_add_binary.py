# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        
        
        if len(a) > len(b):
            b = "0" * (len(a)-len(b)) + b
        else:
            a = "0" * (len(b)-len(a)) + a

        ans = ""
        c = 0

        for i in xrange(len(a)-1, -1, -1):
            val = int(a[i]) + int(b[i]) + c
            r, c = val % 2, int(val >= 2)
            ans = str(r) + ans

        if c == 1:
            ans = "1" + ans

        return ans


            