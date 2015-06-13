# -*- coding: utf-8 -*-
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        from math import floor
        from collections import defaultdict

        dic = defaultdict(int)
        flr = int(len(nums)/2)
        for n in nums:
            dic[n] += 1
            if dic[n] > flr:
                return n
