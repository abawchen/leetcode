import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.077_combinations', fromlist='*')


class Test(unittest.TestCase):


    def test_combine(self):

        s = solutions.Solution()

        n, k = 4, 0
        self.assertEqual(s.combine(n, k), [[]])

        n, k = 4, 1
        self.assertEqual(s.combine(n, k), [[4], [3], [2], [1]])

        n, k = 4, 2
        self.assertEqual(s.combine(n, k), [[3, 4], [2, 4], [2, 3], [1, 4], [1, 3], [1, 2]])

        n, k = 4, 3
        self.assertEqual(s.combine(n, k), [[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]])

        n, k = 4, 4
        self.assertEqual(s.combine(n, k), [[1, 2, 3, 4]])



if __name__ == '__main__':
    unittest.main()
