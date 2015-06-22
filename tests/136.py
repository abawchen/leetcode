import unittest
import sys
sys.path.append('./')

# http://stackoverflow.com/questions/147507/how-does-one-do-the-equivalent-of-import-from-module-with-pythons-import
solutions = __import__('solutions.136_single_number', fromlist='*')


class Test021(unittest.TestCase):

    def test_singleNumber(self):
        s = solutions.Solution()

        nums = [1, 2, 3, 3, 2]
        self.assertEqual(s.singleNumber(nums), 1)


        nums = [1, 2, 3, 3, 2, 4, 4, 1, 5]
        self.assertEqual(s.singleNumber(nums), 5)

        nums = [1, 2, 3, 3, 2, 4, 4, 1, 5, -1, 5]
        self.assertEqual(s.singleNumber(nums), -1)

        nums = [1]
        self.assertEqual(s.singleNumber(nums), 1)


if __name__ == '__main__':
    unittest.main()

