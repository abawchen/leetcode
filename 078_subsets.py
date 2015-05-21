# Given a set of distinct integers, nums, return all possible subsets.
# Note:
#     Elements in a subset must be in non-descending order.
#     The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,3], a solution is:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if not nums:
            return []

        if len(nums) == 1:
            return [[], [nums[0]]]

        return self._subsets(sorted(nums))


    def _subsets(self, nums):
        

        if len(nums) == 2:
            return [[], [nums[0]], [nums[0], nums[1]], [nums[1]]]

        s = self._subsets(nums[1:])
        return [([nums[0]] + n) for n in s] + s

s = Solution()
print s.subsets([])
print s.subsets([1])
# print s.subsets([1, 2])
# print s.subsets([1, 3, 2])
# print s.subsets([1, 3, 2, 4]), len(s.subsets([1, 3, 2, 4]))
# print s.subsets([4,1,0])


