import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.059_spiral_matrix_ii', fromlist='*')


class Test(unittest.TestCase):

    def test_generateMatrix(self):
        s = solutions.Solution()

        n = 1
        matrix = [
            [ 1 ]
        ]
        self.assertEquals(s.generateMatrix(n), matrix)

        n = 2
        matrix = [
            [ 1, 2 ],
            [ 4, 3 ]
        ]
        self.assertEquals(s.generateMatrix(n), matrix)

        n = 3
        matrix = [
            [ 1, 2, 3 ],
            [ 8, 9, 4 ],
            [ 7, 6, 5 ]
        ]
        self.assertEquals(s.generateMatrix(n), matrix)


        n = 4
        matrix = [
            [  1,  2, 3,  4 ],
            [ 12, 13, 14, 5 ],
            [ 11, 16, 15, 6 ],
            [ 10,  9,  8, 7 ]
        ]
        self.assertEquals(s.generateMatrix(n), matrix)


if __name__ == '__main__':
    unittest.main()
