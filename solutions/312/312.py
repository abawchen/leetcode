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



def toKey(nums):
    return "-".join([str(n) for n in nums])


class Node:

    def __init__(self, nums: list[int], key: str, val: int, parent=None):
        self.nums = nums
        self.length = len(nums)
        self.key = key
        self.val = val
        self.sub = 0
        self.parent = parent

class Solution:

    def maxOfThree(self, nums):
        return nums[0]*nums[1]*nums[2] + nums[0]*nums[-1] + max(nums[0], nums[-1])

    def maxCoins(self, nums):
        nums = list(filter(lambda num: num > 0, nums))
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0]*nums[1] + max(nums)
        if len(nums) == 3:
            return self.maxOfThree(nums)

        root = Node(nums, toKey(nums), 0)
        visits = {root.key: root}
        stack = [root]

        while len(stack) != 0:
            cur = stack.pop()
            # print("cur:", cur.key)
            if cur.length == 3:
                cur.sub = self.maxOfThree(cur.nums)
                # print("|", cur.sub, cur.val)
                while cur.parent != None and cur.val + cur.sub > visits[cur.parent.key].sub:
                    visits[cur.parent.key].sub = cur.val + cur.sub
                    cur = visits[cur.parent.key]
                continue

            for i in range(1, len(cur.nums)-1):
                rests = cur.nums[:i] + cur.nums[i+1:]
                val = cur.nums[i-1]*cur.nums[i]*cur.nums[i+1]
                key = toKey(rests)
                if key not in visits:
                    # print(i, cur.nums[i-1], cur.nums[i], cur.nums[i+1])
                    # print("key:", key, "val:", val)
                    node = Node(rests, key, val, cur)
                    visits[key] = node
                    stack.append(node)
                else:
                    node = visits[key]
                    node.val = max(node.val, val)
                    node.parent = cur
                    # print("node.key", node.key, node.val, node.sub)
                    # print("cur.key", cur.key, cur.val, cur.sub)
                    # print("val", val)
                    # node
                    # cur.val = val

                    # cur.sub = max(cur.sub, val + visits[key].sub)

                    # cur.sub = max(cur.sub + cur.val, visits[key].sub)
                    # print("kkkkk", key, sub, val, visits[key].val, visits[key].sub)
                    while node.parent != None and node.val + node.sub > visits[node.parent.key].sub:
                        visits[node.parent.key].sub = node.val + node.sub
                        # print("node.parent.key", node.parent.key, visits[node.parent.key].val, visits[node.parent.key].sub)
                        node = visits[node.parent.key]
                    continue
        # print(visits)
        # for key, node in visits.items():
        #     print(key, node.val, node.sub)
        return root.sub


class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

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
        nums = [9,76,64,21,97,60,5]
        expected = 1088290
        got = self.solution.maxCoins(nums)
        self.assertEqual(expected, got)

if __name__ == '__main__':
    unittest.main()
