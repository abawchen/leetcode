import unittest
from operator import truediv
import sys
sys.path.append('./')

solutions = __import__('solutions.034_search_for_a_range', fromlist='*')


class Test029(unittest.TestCase):

    def test_searchRange(self):
        s = solutions.Solution()

        nums, target = [5, 7, 7, 8, 8, 10], 8
        self.assertEqual(s.searchRange(nums, target), [3, 4])


        nums, target = [5, 7, 7, 8, 8, 8, 8, 8, 10], 8
        self.assertEqual(s.searchRange(nums, target), [3, 7])

        nums, target = [5, 7, 7, 8, 8, 8, 8, 8, 10], 5
        self.assertEqual(s.searchRange(nums, target), [0, 0])


        nums, target = [5, 7, 7, 8, 8, 8, 8, 8, 10], 6
        self.assertEqual(s.searchRange(nums, target), [-1, -1])

        nums, target = [5, 7, 7, 8, 8, 8, 8, 8, 10], 15
        self.assertEqual(s.searchRange(nums, target), [-1, -1])

        nums, target = [0, 0, 2, 3, 4, 4, 4, 5], 5
        self.assertEqual(s.searchRange(nums, target), [7, 7])

        nums, target = [1], 1
        self.assertEqual(s.searchRange(nums, target), [0, 0])
        
if __name__ == '__main__':
    unittest.main()
