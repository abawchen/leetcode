import unittest


class Solution:

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        right = 0
        left = 0
        for num in weights:
            right += num
            if num > left:
                left = num

        if days == 1:
            return right

        while left != right:
            mid = int((left+right)/2)
            group = 0
            accu = 0
            for i, num in enumerate(weights):
                cur = accu + num
                if cur == mid:
                    group += 1
                    accu = 0
                elif cur < mid:
                    if i == len(weights) - 1:
                        group += 1
                    else:
                        accu = cur
                else:
                    group += 1
                    if i == len(weights) - 1:
                        group += 1
                    else:
                        accu = num

            if group > days:
                # too many group, mid is too small
                if left == mid:
                    left = right
                else:
                    left = mid
            else:
                # too less group, mid is too big
                right = mid

        return right


class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        weights = [1,2,3,4,5,6,7,8,9,10]
        days = 5
        expected = 15
        got = self.solution.shipWithinDays(weights, days)
        self.assertEqual(expected, got)

    def test_02(self):
        weights = [3,2,2,4,1,4]
        days = 3
        expected = 6
        got = self.solution.shipWithinDays(weights, days)
        self.assertEqual(expected, got)

    def test_03(self):
        weights = [1,2,3,1,1]
        days = 4
        expected = 3
        got = self.solution.shipWithinDays(weights, days)
        self.assertEqual(expected, got)

if __name__ == '__main__':
    unittest.main()
