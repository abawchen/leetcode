# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
# Note:
#     Elements in a subset must be in non-descending order.
#     The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,2], a solution is:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        if not nums:
            return []

        return self._subsets(sorted(nums))


    def _subsets(self, nums):
        if len(nums) <= 1:
            return [] if len(nums) == 0 else [[], [nums[0]]]

        idx = 1
        dup = False
        for i in xrange(1, len(nums)):
            if nums[i] != nums[0]:
                break
            idx = i
            dup = True

        if dup:
            sub = self._subsets(nums[(idx+1):])
            if sub:
                l = []
                for s in [[nums[0]] * n for n in xrange(1, idx+2)]:
                    l.extend([(s + n) for n in sub])
                return sub + l
            else:
                return [[nums[0]] * n for n in xrange(idx+2)]
        else:
            sub = self._subsets(nums[1:])
            return sub + [([nums[0]] + n) for n in sub]

s = Solution()

# print s.subsetsWithDup([])
# print s.subsetsWithDup([1])
# print s.subsetsWithDup([1, 1])
# # [[], [1], [1, 1]]

# print s.subsetsWithDup([1, 2, 2])
# # [[], [2], [2, 2], [1], [1, 2], [1, 2, 2]]

# print s.subsetsWithDup([1, 2, 2, 2])
# [[], [2], [2, 2], [2, 2, 2], [1], [1, 2], [1, 2, 2], [1, 2, 2, 2]]

# print s.subsetsWithDup([1, 2, 1, 2, 2])
# [[], [2], [2, 2], [2, 2, 2], 
#  [1], [1, 2], [1, 2, 2], [1, 2, 2, 2], 
#  [1, 1], [1, 1, 2], [1, 1, 2, 2], [1, 1, 2, 2, 2]
# ]

print s.subsetsWithDup([1, 2, 1, 2, 2, 3, 3])
[
 [], [3], [3, 3], 
 [2], [2, 3], [2, 3, 3],
 [2, 2], [2, 2, 3], [2, 2, 3, 3], 
 [2, 2, 2], [2, 2, 2, 3], [2, 2, 2, 3, 3], 
 [1], [1, 3], [1, 3, 3], 
 [1, 2], 
 [1, 2, 3], 
 [1, 2, 3, 3], 
 [1, 2, 2], 
 [1, 2, 2, 3], 
 [1, 2, 2, 3, 3], 
 [1, 2, 2, 2], 
 [1, 2, 2, 2, 3], 
 [1, 2, 2, 2, 3, 3], 
 [1, 1], 
 [1, 1, 3], 
 [1, 1, 3, 3], 
 [1, 1, 2], 
 [1, 1, 2, 3], 
 [1, 1, 2, 3, 3], 
 [1, 1, 2, 2], 
 [1, 1, 2, 2, 3], 
 [1, 1, 2, 2, 3, 3], 
 [1, 1, 2, 2, 2], 
 [1, 1, 2, 2, 2, 3], 
 [1, 1, 2, 2, 2, 3, 3]
]

# print s.subsetsWithDup([1, 2])
# print s.subsetsWithDup([1, 2, 3])
# print s.subsetsWithDup([1, 3, 2, 4]), len(s.subsetsWithDup([1, 3, 2, 4]))