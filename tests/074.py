import unittest
from operator import truediv
import sys
sys.path.append('./')

solutions = __import__('solutions.074_search_a_2d_matrix', fromlist='*')


class Test(unittest.TestCase):

    def test_divide(self):
        s = solutions.Solution()

        matrix = [
          [1,   3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 50]
        ]
        target = 3
        self.assertTrue(s.searchMatrix(matrix, target))


        target = 11
        self.assertTrue(s.searchMatrix(matrix, target))

        target = 16
        self.assertTrue(s.searchMatrix(matrix, target))

        target = 50
        self.assertTrue(s.searchMatrix(matrix, target))

        target = 100
        self.assertFalse(s.searchMatrix(matrix, target))

        target = 8
        self.assertFalse(s.searchMatrix(matrix, target))

        matrix = [
          [1]
        ]
        target = 1
        self.assertTrue(s.searchMatrix(matrix, target))

        
if __name__ == '__main__':
    unittest.main()
