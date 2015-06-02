# Given a collection of numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1]. 

# [1,2] have the following permutations:
# [1,2], [2,1]


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        elif len(nums) == 2:
            return [nums, [nums[1], nums[0]]]

        permutations = []
        for i in xrange(len(nums)):
            permutations.extend([ [nums[i]] + p for p in self.permute(nums[0:i] + nums[i+1:len(nums)]) ])

        return permutations



