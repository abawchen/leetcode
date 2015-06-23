import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.036_valid_sudoku', fromlist='*')


class Test(unittest.TestCase):

    def test_searchInsert(self):
        s = solutions.Solution()

        board = [
            ['5', '3', '.',   '.', '7', '.',   '.', '.', '.'],
            ['6', '.', '.',   '1', '9', '5',   '.', '.', '.'],
            ['.', '9', '8',   '.', '.', '.',   '.', '.', '.'],

            ['.', '.', '.',   '.', '.', '.',   '.', '.', '.'],
            ['.', '.', '.',   '.', '.', '.',   '.', '.', '.'],
            ['.', '.', '.',   '.', '.', '.',   '.', '.', '.'],

            ['.', '.', '.',   '.', '.', '.',   '.', '.', '.'],
            ['.', '.', '.',   '.', '.', '.',   '.', '.', '.'],
            ['.', '.', '.',   '.', '.', '.',   '.', '.', '.'],
        ]
        self.assertEqual(s.isValidSudoku(board), True)


if __name__ == '__main__':
    unittest.main()
