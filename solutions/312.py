# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/burst-balloons/description/

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums <= 4):
            return self._maxCoins(nums)

    def _maxCoins(self, coins=0, nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            coin, nums = self.burstBalloon(nums, 1)
        else:
            coin, nums = self.burstBalloon(nums, 2)

    def burstBalloon(self, nums, i):
        left = 1 if i == 0 else nums[i-1]
        right = 1 if i == len(nums)-1 else nums[i+1]
        num = nums.pop(i)
        return (left * num * right, nums)
