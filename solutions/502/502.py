import unittest
import fixtures

class Solution:

    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects = sorted(zip(capital, profits), key = lambda p : p[0])
        count = 0
        for r in range(k):
            profit = 0
            idx = -1
            for i, p in enumerate(projects):
                if w >= p[0]:
                    if p[1] >= profit:
                        idx = i
                        profit = p[1]
                else:
                    break
            if idx == -1:
                break
            else:
                projects.pop(idx)
                w += profit
                count += 1
                if idx == len(projects):
                    break

        if count < k and idx != -1:
            projects = sorted(projects, key = lambda p: -p[1])
            w += sum([p[1] for p in projects[:(k-count)]])
              
        return w



class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        k = 2
        w = 0
        profits = [1,2,3]
        capital = [0,1,1]
        expected = 4
        got = self.solution.findMaximizedCapital(k, w, profits, capital)
        self.assertEqual(expected, got)

    def test_02(self):
        k = 3
        w = 0
        profits = [1,2,3]
        capital = [0,1,2]
        expected = 6
        got = self.solution.findMaximizedCapital(k, w, profits, capital)
        self.assertEqual(expected, got)

    def test_03(self):
        k = 3
        w = 10
        profits = [1,2,3]
        capital = [0,1,2]
        expected = 16
        got = self.solution.findMaximizedCapital(k, w, profits, capital)
        self.assertEqual(expected, got)

    def test_04(self):
        k = 3
        w = 0
        profits = [1,2,3]
        capital = [4,1,2]
        expected = 0
        got = self.solution.findMaximizedCapital(k, w, profits, capital)
        self.assertEqual(expected, got)

    def test_05(self):
        k = 100000
        w = 100000
        profits = fixtures.profits_05
        capital = fixtures.capital_05
        expected = 1000100000
        got = self.solution.findMaximizedCapital(k, w, profits, capital)
        self.assertEqual(expected, got)

    def test_06(self):
        k = 2
        w = 0
        profits = [1,2,3]
        capital = [0,9,10]
        expected = 1
        got = self.solution.findMaximizedCapital(k, w, profits, capital)
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()
