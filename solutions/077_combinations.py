# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# For example,
# If n = 4 and k = 2, a solution is:

# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):

        if n == 0 or k == 0:
            return [[]]

        stack = []
        nums = [ x+1 for x in range(n) ]
        for i in xrange(n-k+1):
            stack.append(([i+1], k-1, nums[i+1:]))

        ans = []
        while stack:
            c, k, r = stack.pop()
            if k == 0:
                ans.append(c)
            else:
                for i in xrange(len(r)-k+1):
                    stack.append((c+[r[i]], k-1, r[i+1:]))

        return ans