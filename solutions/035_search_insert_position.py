# -*- coding: utf-8 -*-
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0 


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        return self._binarySearch(nums, target, 0, len(nums)-1)

    # @param {integer[]} nums
    # @param {integer} target
    # @param {integer} start(index)
    # @param {integer} end(index)
    # @return {integer}
    def _binarySearch(self, nums, target, start, end):
        if start > end:
            return start

        mid = (start+end)/2

        if nums[mid] == target:
            return mid

        return self._binarySearch(nums, target, start, mid-1) if nums[mid] > target else self._binarySearch(nums, target, mid+1, end)