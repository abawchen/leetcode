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


class Ballon:

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class Solution:

    def maxCoins(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0]*nums[1] + max(nums)

        coins = 0
        begin = Ballon(1, None, None)
        end = Ballon(1, None, None)
        left = begin
        biggest = Ballon(0, None, None)
        for i, n in enumerate(nums):
            if n == 0:
                continue
            elif n == 1:
                if i == len(nums)-1:
                    coins += left.value
                else:
                    coins += left.value * nums[i+1]
            else:
                ballon = Ballon(n, left, None)
                left.right = ballon
                left = ballon
                if ballon.value > biggest.value:
                    biggest = ballon
        left.right = end
        end.left = left
        """
        current = begin
        while current is not None:
            print(current.value)
            current = current.right
        """
        print(coins)
        while biggest.left != begin \
            and biggest.left.left != begin:
            left = biggest.left
            coins += biggest.value * left.value * left.left.value
            left.left.right = biggest
            biggest.left = left.left
            print(coins)

        while biggest.right != end \
            and biggest.right.right != end:
            right = biggest.right
            print(biggest.value, right.value, right.right)
            coins += biggest.value * right.value * right.right.value
            right.right.left = biggest
            biggest.right = right.right

        if biggest.left == begin:
            coins += biggest.value * biggest.right.value + biggest.value
        elif biggest.right == end:
            coins += biggest.value * biggest.left.value + biggest.value
        else:
            coins += biggest.value * biggest.left.value * biggest.right.value \
                + biggest.left.value * biggest.right.value \
                + max(biggest.left.value, biggest.right.value)

        return coins

    '''
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(filter(lambda n: n != 0, nums))
        from collections import defaultdict
        d = defaultdict(list)
        begin = Ballon(1, None, None)
        end = Ballon(1, None, None)
        left = begin
        for i, n in enumerate(nums):
            if n != 0:
                ballon = Ballon(n, left, None)
                left.right = ballon
                left = ballon
                d[n].append(ballon)
        left.right = end
        end.left = left

        coins = 0
        ones = d.pop(1, [])
        total = len(nums)
        for ballon in ones:
            coins += ballon.left.value * ballon.value * ballon.right.value
            ballon.left.right = ballon.right
            ballon.right.left = ballon.left
            total -= 1

        sort = sorted(d.keys())
        for n in sort:
            for ballon in d[n]:
                if total > 3 and (ballon == begin.right or ballon == end.left):
                    continue
                if total == 3:
                    center = begin.right.right
                    coins += center.value * center.left.value * center.right.value
                    coins += center.left.value * center.right.value + max(center.left.value, center.right.value)
                    return coins
                value = (ballon.left.value * ballon.value * ballon.right.value)
                coins += value
                ballon.left.right = ballon.right
                ballon.right.left = ballon.left
                total -= 1
        return coins
    '''
