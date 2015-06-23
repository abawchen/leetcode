import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.035_search_insert_position', fromlist='*')


class Test(unittest.TestCase):

    def test_searchInsert(self):
        s = solutions.Solution()

        nums, target = [1, 3, 5, 6], 5
        self.assertEqual(s.searchInsert(nums, target), 2)

        nums, target = [1, 3, 5, 6], 2
        self.assertEqual(s.searchInsert(nums, target), 1)

        nums, target = [1, 3, 5, 6], 7
        self.assertEqual(s.searchInsert(nums, target), 4)

        nums, target = [1, 3, 5, 6], 0
        self.assertEqual(s.searchInsert(nums, target), 0)

if __name__ == '__main__':
    unittest.main()
