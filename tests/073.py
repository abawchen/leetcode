import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.073_set_matrix_zeroes', fromlist='*')


class Test(unittest.TestCase):

    def test_setZeroes(self):
        s = solutions.Solution()

        matrix = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        result = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
        self.assertEqual(s.setZeroes(matrix), result)

        matrix = [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1]
        ]
        result = [
            [1, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(s.setZeroes(matrix), result)


        matrix = [
            [0, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1]
        ]
        result = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(s.setZeroes(matrix), result)


        matrix = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 0, 1]
        ]
        result = [
            [0, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0]
        ]
        self.assertEqual(s.setZeroes(matrix), result)


        
if __name__ == '__main__':
    unittest.main()
