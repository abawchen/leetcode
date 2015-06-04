import unittest
import sys
sys.path.append('./')
solutions = __import__('solutions.048_rotate_image', fromlist='*')


class Test048(unittest.TestCase):

    def test_calPairs(self):
        s = solutions.Solution()
        self.assertEqual(s.calPairs(1, 0), [])
        self.assertEqual(s.calPairs(2, 0), [[(0, 0), (0, 1), (1, 1), (1, 0)]])
        self.assertEqual(s.calPairs(2, 1), [[(1, 1), (1, 2), (2, 2), (2, 1)]])
        self.assertEqual(s.calPairs(3, 0), [[(0, 0), (0, 2), (2, 2), (2, 0)], [(0, 1), (1, 2), (2, 1), (1, 0)]])
        self.assertEqual(s.calPairs(4, 0), [[(0, 0), (0, 3), (3, 3), (3, 0)], [(0, 1), (1, 3), (3, 2), (2, 0)], [(0, 2), (2, 3), (3, 1), (1, 0)]])
    
    def test_rotate(self):
        s = solutions.Solution()


        matrix = [
            [1]
        ]
        self.assertEqual(s.rotate(matrix), [
            [1]
        ])

        matrix = [
            [1, 2],
            [3, 4]
        ]
        self.assertEqual(s.rotate(matrix), [
            [3, 1],
            [4, 2]
        ])

        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(s.rotate(matrix), [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3],
        ])

        matrix = [
            [ 1,  2,  3,  4],
            [ 5,  6,  7,  8],
            [ 9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.assertEqual(s.rotate(matrix), [
            [13,  9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ])

        matrix = [
            [ 1,  2,  3,  4,  5],
            [ 6,  7,  8,  9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
        self.assertEqual(s.rotate(matrix), [
            [21, 16, 11,  6, 1],
            [22, 17, 12,  7, 2],
            [23, 18, 13,  8, 3],
            [24, 19, 14,  9, 4],
            [25, 20, 15, 10, 5],
        ])



if __name__ == '__main__':
    unittest.main()