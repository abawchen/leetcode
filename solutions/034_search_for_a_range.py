# Given a sorted array of integers, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4]. 


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        if nums[0] > target or nums[-1] < target:
            return [-1, -1]

        # O(n)
        start, end, i, j = -1, -1, 0, len(nums) - 1
        while i <= j:

            if nums[i] == target:
                start = i
            else:
                i += 1
            
            if nums[j] == target:
                end = j
            else:
                j -= 1

            if start != -1 and end != -1:
                break

        return [start, end]