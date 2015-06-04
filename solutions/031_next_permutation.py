# -*- coding: utf-8 -*-
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if not nums:
            return

        target = -1
        for i in xrange(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                target = i
                break

        if target == -1:
            nums[:] = list(reversed(nums))
            # return nums # for test
            return

        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] > nums[target]:
                break

        v1, v2 = nums[target], nums.pop(i)
        if target < len(nums)-1:
            i, tail = 0, list(reversed(nums[target+1:]))
            while i < len(tail) and v1 > tail[i]:
                i += 1
            tail.insert(i, v1)
        else:
            tail = [v1]

        nums[:] = nums[:target] + [v2] + tail