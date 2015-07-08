#  A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2. 

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):

        if not s or s[0] == '0':
            return 0
        
        dp = [1] + [0]*(len(s)-1)
        pool = set([ str(n+1) for n in xrange(26) ])

        for i in xrange(1, len(dp)):
            if dp[i-1] and s[i] in pool:
                dp[i] = dp[i-1]

            if s[i-1:i+1] in pool:
                dp[i] += dp[i-2] if i >= 2 else 1

            if not dp[i]:
                return 0

        return dp[-1]
