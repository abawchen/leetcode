import unittest
from collections import defaultdict

class Solution:

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dps = []

        dp = defaultdict(int, {nums[0]: 1})
        dp[-nums[0]] += 1
        dps.append(dp)

        for i in range(1, len(nums)):
            dp = defaultdict(int)
            for key, val in dps[i-1].items():
                dp[key+nums[i]] += val
                dp[key-nums[i]] += val
            dps.append(dp)

        return dps[-1].get(target, 0)

class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        nums = [1,1,1,1,1]
        target = 3
        got = self.solution.findTargetSumWays(nums, target)
        expected = 5
        self.assertEqual(expected, got)

    def test_01(self):
        nums = [1]
        target = 1
        got = self.solution.findTargetSumWays(nums, target)
        expected = 1
        self.assertEqual(expected, got)

    def test_03(self):
        nums = [1,0]
        target = 1
        got = self.solution.findTargetSumWays(nums, target)
        expected = 2
        self.assertEqual(expected, got)

    def test_04(self):
        nums = [0,0,0,0,0,0,0,0,1]
        target = 1
        got = self.solution.findTargetSumWays(nums, target)
        expected = 256
        self.assertEqual(expected, got)

    def test_05(self):
        nums = [0]
        target = 0
        got = self.solution.findTargetSumWays(nums, target)
        expected = 2
        self.assertEqual(expected, got)

if __name__ == '__main__':
    unittest.main()