import unittest


class Solution:
    def splitArray(self, nums: list[int], m: int) -> int:
        accu = 0
        dps = [[]]
        for num in (nums):
            accu += num
            dps[0].append(accu)

        for i in range(1, m):
            dp = []
            for j in range(len(nums)):
                if j < i:
                    dp.append(dps[i-1][j])
                    continue
                gmin = dps[0][-1]
                for k in range(j):
                    lmax = max(dps[i-1][k], sum(nums[k+1:j+1]))
                    if lmax < gmin:
                        gmin = lmax
                dp.append(gmin)    

            dps.append(dp)

        return dps[m-1][len(nums)-1]



class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        nums = [7,2,5,10,8]
        m = 2
        expected = 18
        got = self.solution.splitArray(nums, m)
        self.assertEqual(expected, got)

    def test_02(self):
        nums = [7,2,5,10,8]
        m = 3
        expected = 14
        got = self.solution.splitArray(nums, m)
        self.assertEqual(expected, got)

    def test_03(self):
        nums = [4, 4, 1]
        m = 3
        expected = 4
        got = self.solution.splitArray(nums, m)
        self.assertEqual(expected, got)

    def test_04(self):
        nums = [1, 2, 3, 4, 5]
        m = 2
        expected = 9
        got = self.solution.splitArray(nums, m)
        self.assertEqual(expected, got)



if __name__ == '__main__':
    unittest.main()
