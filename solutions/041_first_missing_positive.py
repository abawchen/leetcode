# Given an unsorted integer array, find the first missing positive integer.

# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.

# Your algorithm should run in O(n) time and uses constant space. 


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):

        i, count, expected = 0, 0, 1

        while i < len(nums) and count < len(nums)-1:
            val = nums[i]
            while val != i+1 and val > 0 and val <= len(nums) and val != nums[val-1]:
                nums[i], nums[val-1] = nums[val-1], val
                val, count = nums[i], count+1
            i += 1
       
        for n in nums:
            if n < 0:
                continue

            if n != expected:
                return expected

            expected += 1

        return expected
