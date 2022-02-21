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


def key(i, j):
    return f'{i}-{j}'



class Solution:

    def maxCoins(self, nums):
        dp = {}
        nums = [1] + nums + [1]

        def burst(i, j):
            if ((i, j)) in dp:
                return dp[(i, j)]

            coins = 0
            for k in range(i, j+1):
                head = burst(i, k-1)
                body = nums[i-1]*nums[k]*nums[j+1]
                tail = burst(k+1, j)
                coins = max(coins, head + body + tail)
            dp[(i, j)] = coins

            return coins

        return burst(1, len(nums)-2)


class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_00(self):
        nums = [3,1,5]
        expected = 35
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)

    def test_01(self):
        nums = [10]
        expected = 10
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)

        nums = [3,8]
        expected = 3*8 + 8
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)

        nums = [3,10,3]
        expected = 90 + 9 + 3
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)

        nums = [3, 5, 8]
        expected = 152
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)

        nums = [1, 5, 8]
        expected = 56
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)

        nums = [1, 3, 8]
        expected = 40
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)

    def test_02(self):
        nums = [3,1,5,8]
        print("\n", nums)
    #     nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
    #     coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
        expected = 167
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)
        self.assertEqual(expected, self.solution.maxCoins([0,3,1,5,8]))
        self.assertEqual(expected, self.solution.maxCoins([3,0,1,5,8]))

        self.assertEqual(160, self.solution.maxCoins([1,3,5,8]))
        # [1,3,5,8] --> [1,3,8] --> [1,8] --> [8]
        #   3*5*8          24         8        8 = 160


        nums = [3,1,2,5,8]
        expected = 6 + 30 + 152
        got = self.solution.maxCoins([3,1,2,5,8])
        self.assertEqual(expected, got)

        nums = [1,2,5,8]
        print("qq", self.solution.maxCoins(nums))

        nums = [1,3,5,8]
        print("qq", self.solution.maxCoins(nums))

        nums = [1,3, 2,8]
        print("qq", self.solution.maxCoins(nums))
      

    def test_03(self):
        self.assertEqual(self.solution.maxCoins([1,3,2,5,8]), 190)
        self.assertEqual(self.solution.maxCoins([9,76,64,21]), 116718) # (102144 + 14574)
        self.assertEqual(self.solution.maxCoins([9,76,21]), 14574)
        self.assertEqual(self.solution.maxCoins([76,64,21,21]), 137332) # (64*76*21 + 35188)
    
    def test_04(self):
        nums = [9,76,97,60,5]
        print("\n", nums)
        # [9,76,97,60,5] val: 0 sub: 486114
        # [9,97,60,5] val: 66348 sub: 70767
        # [9,76,60,5] val: 442320 sub: 43794
        # [9,76,97,5] val: 29100 sub: 70767

        got = self.solution.maxCoins(nums)  
        
        nums = [9,76,64,97,60,5]
        # [9,76,97,60,5] val: 471808(76*64*97) sub: 542575
        print("\n", nums)
        got = self.solution.maxCoins(nums)  
        
    def test_05(self):
        nums = [9,76,64,21,97,60,5]
        # [9,76,64,97,60,5] val: 130368 sub: 1014383

        print("\n", nums)
        expected = 1088290
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)


    def test_06(self):
        nums = [35,16,83,87,84,59,48,41]
        expected = 1583373
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)


    def test_07(self):
        print(self.solution.maxCoins([2,3,7,9]))
        # nums = [2,3,9,1]
        # print("\n", nums)
        # expected = 76
        # got = self.solution.maxCoins(nums)
        # self.assertEqual(expected, got)

        nums = [2,3,7,9,1]
        print("\n", nums)
        expected = 279
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)

    def test_08(self):
        nums = [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]
        expected = 3394
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)

    def test_09(self):
        nums = [21,47,65,65,26,17,80,25,92,42,1,5,20,75,98,42,61,76,2,95,76,12,87,87,71,71,38,95,49,61,85,50,8,83,36,16,12,49,51,85,7,29,26,17,61,57,34,89,89,16,9,79,11,75,65,61,78,45,67,14,59,21,67,82,27,14,36,94,65,52,38,89,29,75,52,28,87,22,4,12,20,41,63,78,30,92,26,40,0,52,65,51,30,34,71,64,74,48,49,80,45,3,65,27,90,23,88,56,64,97,88,97,70,25,93,41,63,0,18,74,41,41,63,72,29,97,24,46,3,50,32,16,95,80,98,14,27,25,81,34,27,62,84,2,93,72,34,61,92,94,59,88,75,12,3,10,60,22,71,47,49,1,39,48,2,99,53,32,32,18,51,4,43,77,78,62,42,76,82,70,57,67,37,87,75,72,0,42,43,73,67,91,22,14,69,38,100,40,100,15,26,91,1,67,28,58,92,16,11,78,7,53,28,65,48,90,78,92,49,78,38,3,79,13,59,41,7,8,27,18,71,97,71,14,61,58,86,84,0,8,97,51,65,69,39,24,20,62,45,97,42,12,92,52,7,46,8,56,20,22,11,12,81,27,12,15,19,1,84,14,38,29,69,42,44,66,68,22,24,94,31,62,36,37,75,6,7,26,69,17,67,52,12,100,88,10,16,40,93,62]
        print(len(nums))
        self.solution.maxCoins(nums)

if __name__ == '__main__':
    unittest.main()
