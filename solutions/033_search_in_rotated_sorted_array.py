# Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        pre, suf = self._split(nums, 0, len(nums)-1)
        if not pre or target > pre[-1] or target < pre[0]:
            r = self._binarySearch(suf, target, 0, len(suf)-1)
            return r+len(pre) if r != -1 else -1
        
        return self._binarySearch(pre, target, 0, len(pre)-1)


    def _split(self, nums, start, end, sp=0):
        if start >= end:
            return nums[:sp], nums[sp:]

        mid = (start+end)/2
        if nums[start] <= nums[mid] and nums[mid] <= nums[end]:
            return nums[:sp], nums[sp:]

        if nums[start] > nums[mid]:
            return self._split(nums, start, mid-1, mid)
        else:
            return self._split(nums, mid+1, end, mid+1)

    def _binarySearch(self, nums, target, start, end):
        if start > end:
            return -1

        mid = (start+end)/2

        if nums[mid] == target:
            return mid

        return self._binarySearch(nums, target, start, mid-1) if nums[mid] > target else self._binarySearch(nums, target, mid+1, end)

