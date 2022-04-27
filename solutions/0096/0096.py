import unittest


class Solution:

    def __init__(self):
        self.dp = {
            0:0,
            1:1,
        }

    def numTrees(self, n: int) -> int:
        if n not in self.dp:
            self.dp[n] = 0
            for i in range (1, n+1):
                j, k = i-1, n-i
                self.dp[n] += max(1, self.numTrees(j)) * max(1, self.numTrees(k))

        return self.dp[n]
        

class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        n = 1
        got = self.solution.numTrees(n)
        expected = 1
        self.assertEqual(expected, got)

    def test_02(self):
        n = 2
        got = self.solution.numTrees(n)
        expected = 2
        self.assertEqual(expected, got)

    def test_03(self):
        n = 3
        got = self.solution.numTrees(n)
        expected = 5
        self.assertEqual(expected, got)
        print(self.solution.print())


if __name__ == '__main__':
    unittest.main()