import unittest

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums = sorted(nums)
        ans = 0
        n = None
        accus = []
        
        for i, num in enumerate(nums):
            if len(accus) == 0:
                accus.append(num)
                continue

            diff = num - accus[0]
            if diff <= 1:
                accus.append(num)
                if diff == 1 and n is None:
                    n = i
            else:
                if accus and accus[-1] - accus[0] == 1:
                    ans = max(ans, len(accus))
                
                if n is not None and num - nums[n] == 1:
                    accus = nums[n: i+1]
                    n = i
                else:
                    accus = [num]
                    n = None
                
        if accus and accus[-1] - accus[0] == 1:
            ans = max(ans, len(accus))

        return ans


class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_00(self):
        # nums = [1,3,2,2,5,2,3,7]
        # nums = [1,2,2,2,3,3,5,7]
        nums = []
        got = self.solution.findLHS(nums)
        expected = 0
        self.assertEqual(expected, got)

        nums = [1]
        got = self.solution.findLHS(nums)
        expected = 0
        self.assertEqual(expected, got)

        nums = [1,1]
        got = self.solution.findLHS(nums)
        expected = 0
        self.assertEqual(expected, got)

    def test_01(self):
        # nums = [1,3,2,2,5,2,3,7]
        # nums = [1,2,2,2,3,3,5,7]
        nums = [1,3,2,2,5,2,3,7]
        got = self.solution.findLHS(nums)
        expected = 5
        self.assertEqual(expected, got)

    def test_02(self):
        nums = [1,2,3,4]
        got = self.solution.findLHS(nums)
        expected = 2
        self.assertEqual(expected, got)

    def test_03(self):
        nums = [1,1,1,1]
        got = self.solution.findLHS(nums)
        expected = 0
        self.assertEqual(expected, got)

    def test_04(self):
        nums = [1,2,2,1]
        got = self.solution.findLHS(nums)
        expected = 4
        self.assertEqual(expected, got)


    def test_05(self):
        nums = [3,2,1]
        got = self.solution.findLHS(nums)
        expected = 2
        self.assertEqual(expected, got)

    def test_06(self):
        nums = [1,3,5,7,9,11,13,15,17]
        got = self.solution.findLHS(nums)
        expected = 0
        self.assertEqual(expected, got)

    def test_07(self):
        nums = [1,2,3,3,1,-14,13,4]
        got = self.solution.findLHS(nums)
        expected = 3
        self.assertEqual(expected, got)

    def test_08(self):
        nums = [1,4,1,3,1,-14,1,-13]
        got = self.solution.findLHS(nums)
        expected = 2
        self.assertEqual(expected, got)

    def test_09(self):
        nums = [1,2,-1,1,2,5,2,5,2]
        got = self.solution.findLHS(nums)
        expected = 6
        self.assertEqual(expected, got)

    def test_10(self):
        nums = [3,2,2,3,2,1,3,3,3,-2,0,3,2,1,0,3,1,0,1,3,0,3,3]    
        got = self.solution.findLHS(nums)
        expected = 14
        self.assertEqual(expected, got)

    def test_11(self):
        nums = [-3, -3, -2, -1, -1, -1]
        got = self.solution.findLHS(nums)
        expected = 4
        self.assertEqual(expected, got)


    def test_12(self):
        nums = [2,2,2,2,2,2,2,3,1,0,0,0,3,1,-1,0,1,1,0,0,1,1,2,2,2,0,1,2,2,3,2]
        got = self.solution.findLHS(nums)
        expected = 20
        self.assertEqual(expected, got)


    def test_13(self):
        nums = [1,2,3,4,6,5,-5,10,-1,-2,5,4,4,-1,7]
        expected = 5
        got = self.solution.findLHS(nums)
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()