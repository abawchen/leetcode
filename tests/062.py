import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.062_unique_paths', fromlist='*')


class Test(unittest.TestCase):

    def test_uniquePaths(self):
        s = solutions.Solution()

        m, n = 1, 2
        self.assertEquals(s.uniquePaths(m, n), 1)

        m, n = 10, 0
        self.assertEquals(s.uniquePaths(m, n), 0)

        m, n = 1, 1
        self.assertEquals(s.uniquePaths(m, n), 1)

        m, n = 3, 7
        self.assertEquals(s.uniquePaths(m, n), 28)

        m, n = 1, 1
        self.assertEquals(s.uniquePaths(m, n), 1)


        # m, n = 100, 100
        # self.assertEquals(s.uniquePaths(m, n), 100)


if __name__ == '__main__':
    unittest.main()
