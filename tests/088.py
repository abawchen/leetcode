import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.088_merge_sorted_array', fromlist='*')

class Test088(unittest.TestCase):

    def test_merge(self):
        s = solutions.Solution()

        nums1 = []
        nums2 = []
        self.assertEqual(s.merge(nums1, len(nums1), nums2, len(nums2)), [])

        nums1 = [1, 2, 3, 4]
        nums2 = [0, 0, 0, 0]
        self.assertEqual(s.merge(nums1, 4, nums2, 0), [1, 2, 3, 4])

        nums1 = [0, 0, 0, 0]
        nums2 = [1, 2, 3, 4]
        self.assertEqual(s.merge(nums1, 0, nums2, 4), [1, 2, 3, 4])

        nums1 = [1, 2, 3, 0, 0, 0, 0]
        nums2 = [1, 2, 3]
        self.assertEqual(s.merge(nums1, 3, nums2, 3), [1, 1, 2, 2, 3, 3])

        nums1 = [1, 2, 3, 4, 0, 0, 0, 0]
        nums2 = [1, 2, 3, 4]
        self.assertEqual(s.merge(nums1, 4, nums2, len(nums2)), [1, 1, 2, 2, 3, 3, 4, 4])


        nums1 = [1, 2, 3, 3, 3, 4, 0, 0, 0, 0]
        nums2 = [1, 2, 3, 4]
        self.assertEqual(s.merge(nums1, 6, nums2, 4), [1, 1, 2, 2, 3, 3, 3, 3, 4, 4])

        nums1 = [1, 2, 3, 4, 0, 0, 0, 0, 0, 0]
        nums2 = [1, 2, 3, 3, 3, 4]
        self.assertEqual(s.merge(nums1, 4, nums2, 6), [1, 1, 2, 2, 3, 3, 3, 3, 4, 4])


        nums1 = [0, 2, 4, 6, 0, 0, 0, 0, 0, 0, 0, -1]
        nums2 = [1, 3, 5, 7, 9, 10, 11, 0, 0]
        self.assertEqual(s.merge(nums1, 4, nums2, 7), [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11])

        nums1 = [1, 3, 5, 7, 9, 10, 11, 0, 0, 0, 0, 0]
        nums2 = [0, 2, 4, 6]
        self.assertEqual(s.merge(nums1, 7, nums2, 4), [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11])

        self.assertEqual(s.merge([0], 0, [1], 1), [1])

        nums1 = [1, 3, 5, 7, 0, 0, 0, 0]
        nums2 = [0, 2, 4, 6]
        self.assertEqual(s.merge(nums1, 4, nums2, 2), [0, 1, 2, 3, 5, 7])

        nums1 = [1, 3, 5, 7, 0, 0, 0, 0]
        nums2 = [0, 2, 7, 9]
        self.assertEqual(s.merge(nums1, 4, nums2, 4), [0, 1, 2, 3, 5, 7, 7, 9])

        nums1 = [1, 3, 5, 7, 7, 8, 0, 0]
        nums2 = [0, 2, 7, 9]
        self.assertEqual(s.merge(nums1, 6, nums2, 4), [0, 1, 2, 3, 5, 7, 7, 7, 8, 9])

        nums1 = [0, 2, 0, 0, 0, 0, 0]
        nums2 = [1, 3, 5, 7]
        self.assertEqual(s.merge(nums1, 2, nums2, 4), [0, 1, 2, 3, 5, 7])
        

if __name__ == '__main__':
    unittest.main()

