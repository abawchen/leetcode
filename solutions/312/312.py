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

import unittest

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

class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        assert self.solution.maxCoins([10]) == 10
        assert self.solution.maxCoins([3,8]) == 3*8 + 8
        assert self.solution.maxCoins([3,10,3]) == (90 + 9 + 3)
        """
        """
        assert self.solution.maxCoins([3,5,8]) == 152 #(3*5*8 + 3*8 + 8)
        assert self.solution.maxCoins([1,5,8]) == (5 + 40 + 8)
        assert self.solution.maxCoins([8,5,3]) == 152
        assert self.solution.maxCoins([3,1,5,8]) == (15 + 152)
        assert self.solution.maxCoins([0,3,1,5,8]) == 167
        assert self.solution.maxCoins([3,0,1,5,8]) == 167

    def test_02(self):
        pass
        # assert s.maxCoins([3,2,5,8]) == (3*2*5 + 152)
        # assert s.maxCoins([3,5,8]) == 120 + 24 + 8 # 30
        # assert s.maxCoins([3,2,8]) == 48 + 24 + 8  # 80
        # # assert s.maxCoins([3,1,2,5,8]) == (6 + 30 + 152)
        """
        assert s.maxCoins([1,3,5,8]) == (3 + 152)
        assert s.maxCoins([1,3,2,5,8]) == (3 + 30 + 152)
        assert s.maxCoins([9,76,64,21]) == 116718 # (102144 + 14574)
        assert s.maxCoins([9,76,21]) == 14574
        assert s.maxCoins([76,64,21,21]) == 137332 # (64*76*21 + 35188)
        # """
        """
        ==> 先砍 64
            76*64*21 + 76*21*21 + 76*21 + 76
                       ^^^^^^^^
        ==> 先砍 21
            64*21*21 + 76*64*61 + 76*21 + 76
            ^^^^^^^^
        """
        """
        assert s.maxCoins([76,21,21]) == 35188
        assert s.maxCoins([76,64,21]) == 103816
        """

if __name__ == '__main__':
    unittest.main()
