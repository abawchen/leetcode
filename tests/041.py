import unittest
import sys
import random
sys.path.append('./')

solutions = __import__('solutions.041_first_missing_positive', fromlist='*')


class Test(unittest.TestCase):

    def test_firstMissingPositive(self):
        s = solutions.Solution()

        nums = [1, 2, 0]
        self.assertEqual(s.firstMissingPositive(nums), 3)


        # nums = [3, 4, -1, 1]
        nums = [-1, 4, 3, 1]
        self.assertEqual(s.firstMissingPositive(nums), 2)

        
        nums = [5, 6, 7, 8, 10]
        self.assertEqual(s.firstMissingPositive(nums), 1)

        nums = [3, 4, -1, -2, 1, 2, 7]
        self.assertEqual(s.firstMissingPositive(nums), 5)

        nums = [4, 5, 1, 2, 3]
        self.assertEqual(s.firstMissingPositive(nums), 6)


        nums = [9, 10, 1, 3, 4, 5, 6, 7, 8]
        nums = random.sample(range(1, 11, 1), 10)
        
        nums = [4, 1, 5, 10, 7, 6, 2, 9, 3, 8]
        self.assertEqual(s.firstMissingPositive(nums), 11)


        # nums = random.sample(range(1, 21, 1), 20)
        # self.assertEqual(s.firstMissingPositive(nums), 11)

        nums = [3, 8, 18, 17, 10, 12, 1, 4, 19, 11, 16, 6, 5, 20, 15, 14, 2, 7, 13, 9]
        self.assertEqual(s.firstMissingPositive(nums), 21)


        nums = [3, 8, 18, 17, 10, 12, 1, 4, 19, 11, 16, -2, -3, 20, 15, 14, 2, 7, 13, 9]
        self.assertEqual(s.firstMissingPositive(nums), 5)


        nums = [-1, 4, 3, 1, 2, -2, -3, 5, 8]
        self.assertEqual(s.firstMissingPositive(nums), 6)

        nums = [1, 1]
        self.assertEqual(s.firstMissingPositive(nums), 2)


        nums = [1, 2, 3, 1, 2, 5, 4, 4, 5, 5, 6]
        self.assertEqual(s.firstMissingPositive(nums), 7)


if __name__ == '__main__':
    unittest.main()

