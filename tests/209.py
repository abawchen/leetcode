import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.209_minimum_size_subarray_sum', fromlist='*')


class Test(unittest.TestCase):

    def test_minSubArrayLen(self):
        s = solutions.Solution()

        S = 7
        nums = [2, 3, 1, 2, 4, 3]
        self.assertEqual(s.minSubArrayLen(S, nums), 2)

        S = 7
        nums = [2, 3, 1, 2, 4]
        self.assertEqual(s.minSubArrayLen(S, nums), 3)
        
        S = 6
        nums = [2, 3, 1, 2, 4]
        self.assertEqual(s.minSubArrayLen(S, nums), 2)

        S = 3
        nums = [2, 3, 1, 2, 4]
        self.assertEqual(s.minSubArrayLen(S, nums), 1)
        
        S = 4
        nums = [2, 3, 1, 2, 4]
        self.assertEqual(s.minSubArrayLen(S, nums), 1)
        
        S = 5
        nums = [2, 3, 1, 2, 4]
        self.assertEqual(s.minSubArrayLen(S, nums), 2)
        
        S = 5
        nums = [1, 1, 3, 1, 1]
        self.assertEqual(s.minSubArrayLen(S, nums), 3)
        
        S = 5
        nums = [1, 1, 3, 2, 1]
        self.assertEqual(s.minSubArrayLen(S, nums), 2)
        
        S = 5
        nums = [1, 1, 3, 1, 2]
        self.assertEqual(s.minSubArrayLen(S, nums), 3)
        
        S = 10
        nums = [1, 1, 3, 1, 2]
        self.assertEqual(s.minSubArrayLen(S, nums), 0)

        S = 11
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(s.minSubArrayLen(S, nums), 3)

        S = 80
        nums = [10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8]
        self.assertEqual(s.minSubArrayLen(S, nums), 6)
        # [10, 5, 13, 4, 8, 4, 5, 11, 14, 9] 83, 10
        # [13, 4, 8, 4, 5, 11, 14, 9, 16], 84, 9
        # [11, 14, 9, 16, 10, 20] 80, 6

        S = 15
        nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
        self.assertEqual(s.minSubArrayLen(S, nums), 2)

        
if __name__ == '__main__':
    unittest.main()
