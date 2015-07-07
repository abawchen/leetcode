# -*- coding: utf-8 -*-
# The set [1,2,3,…,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):

#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"

# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):

        dp = [1]
        while dp[-1] < k:
            dp.append(dp[-1]*(len(dp)+1))

        nums = [ str(x+1) for x in range(n) ]
        ans = self._getPermutation([], nums, dp, k)
        return ''.join(ans)


    def _getPermutation(self, ans, nums, dp, k):

        i = 0
        while dp[i] < k:
            i += 1

        ans += nums[:-i-1]
        nums = nums[-i-1:]

        if dp[i] == k:
            return ans + list(reversed(nums))

        quotient, remainder = k/dp[i-1], k%dp[i-1]
        if remainder == 0:
            quotient -= 1
            remainder = dp[i-1]

        x = nums[quotient]
        nums.remove(x)
        nums.insert(0, x)

        return self._getPermutation(ans, nums, dp, remainder)
