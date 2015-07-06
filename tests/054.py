import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.054_spiral_matrix', fromlist='*')


class Test(unittest.TestCase):

    def test_spiralOrder(self):
        s = solutions.Solution()

        matrix = [
             [ 1, 2, 3 ],
             [ 4, 5, 6 ],
             [ 7, 8, 9 ]
        ]
        spiral = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEquals(s.spiralOrder(matrix), spiral)


        matrix = [
             [ 1, 2, 3 ],
             [ 7, 8, 9 ]
        ]
        spiral = [1, 2, 3, 9, 8, 7]
        self.assertEquals(s.spiralOrder(matrix), spiral)


        matrix = [
             [1]
        ]
        spiral = [1]
        self.assertEquals(s.spiralOrder(matrix), spiral)


        matrix = [
             [1, 2],
             [3, 4]
        ]
        spiral = [1, 2, 4, 3]
        self.assertEquals(s.spiralOrder(matrix), spiral)


        matrix = [
             [1, 2],
             [2, 5],
             [4, 5],
             [3, 5]
        ]
        spiral = [1, 2, 5, 5, 5, 3, 4, 2]
        self.assertEquals(s.spiralOrder(matrix), spiral)


if __name__ == '__main__':
    unittest.main()
