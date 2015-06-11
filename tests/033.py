import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.033_search_in_rotated_sorted_array', fromlist='*')


class Test033(unittest.TestCase):

    
    def test_search(self):
        s = solutions.Solution()

        nums, target = [1, 3], 0
        self.assertEqual(s.search(nums, target), -1)

        nums, target = [0], 1
        self.assertEqual(s.search(nums, target), -1)

        nums, target = [0], 0
        self.assertEqual(s.search(nums, target), 0)

        nums, target = [0, 1, 2, 3], 0
        self.assertEqual(s.search(nums, target), 0)

        nums, target = [3, 0, 1, 2], 0
        self.assertEqual(s.search(nums, target), 1)

        nums, target = [2, 3, 0, 1], 0
        self.assertEqual(s.search(nums, target), 2)

        nums, target = [1, 2, 3, 0], 0
        self.assertEqual(s.search(nums, target), 3)


        nums, target = [0, 1, 2, 3], 1
        self.assertEqual(s.search(nums, target), 1)

        nums, target = [3, 0, 1, 2], 1
        self.assertEqual(s.search(nums, target), 2)

        nums, target = [2, 3, 0, 1], 1
        self.assertEqual(s.search(nums, target), 3)

        nums, target = [1, 2, 3, 0], 1
        self.assertEqual(s.search(nums, target), 0)

        nums, target = [0, 1, 2, 3], 2
        self.assertEqual(s.search(nums, target), 2)

        nums, target = [3, 0, 1, 2], 2
        self.assertEqual(s.search(nums, target), 3)

        nums, target = [2, 3, 0, 1], 2
        self.assertEqual(s.search(nums, target), 0)

        nums, target = [1, 2, 3, 0], 2
        self.assertEqual(s.search(nums, target), 1)


        nums, target = [0, 1, 2, 3], 4
        self.assertEqual(s.search(nums, target), -1)

        nums, target = [3, 0, 1, 2], 4
        self.assertEqual(s.search(nums, target), -1)

        nums, target = [2, 3, 0, 1], 4
        self.assertEqual(s.search(nums, target), -1)

        nums, target = [1, 2, 3, 0], 4
        self.assertEqual(s.search(nums, target), -1)

        nums, target = [0, 1, 2, 3, 5], 4
        self.assertEqual(s.search(nums, target), -1)

        nums, target = [5, 0, 1, 2, 3], 4
        self.assertEqual(s.search(nums, target), -1)

        nums, target = [3, 5, 0, 1, 2], 4
        self.assertEqual(s.search(nums, target), -1)

        nums, target = [2, 3, 5, 0, 1], 4
        self.assertEqual(s.search(nums, target), -1)

        nums, target = [1, 2, 3, 5, 0], 4
        self.assertEqual(s.search(nums, target), -1)

        nums, target = [6, 7, 1, 2, 3, 4, 5], 6
        self.assertEqual(s.search(nums, target), 0)


    def test_split(self):
        s = solutions.Solution()

        l = [1, 3]
        self.assertEqual(s._split(l, 0, len(l)-1), ([], l))

        l = [0]
        self.assertEqual(s._split(l, 0, len(l)-1), ([], l))

        l = [0, 1]
        self.assertEqual(s._split(l, 0, len(l)-1), ([], [0, 1]))

        l = [1, 0]
        self.assertEqual(s._split(l, 0, len(l)-1), ([1], [0]))

        l = [0, 1, 2]
        self.assertEqual(s._split(l, 0, len(l)-1), ([], l))

        l = [2, 0, 1]
        self.assertEqual(s._split(l, 0, len(l)-1), ([2], [0, 1]))

        l = [1, 2, 0]
        self.assertEqual(s._split(l, 0, len(l)-1), ([1, 2], [0]))


        l = [0, 1, 2, 3]
        self.assertEqual(s._split(l, 0, len(l)-1), ([], l))

        l = [3, 0, 1, 2]
        self.assertEqual(s._split(l, 0, len(l)-1), ([3], [0, 1, 2]))

        l = [2, 3, 0, 1]
        self.assertEqual(s._split(l, 0, len(l)-1), ([2, 3], [0, 1]))

        l = [1, 2, 3, 0]
        self.assertEqual(s._split(l, 0, len(l)-1), ([1, 2, 3,], [0]))

        l = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(s._split(l, 0, len(l)-1), ([], [1, 2, 3, 4, 5, 6, 7]))

        l = [2, 3, 4, 5, 6, 7, 1]
        self.assertEqual(s._split(l, 0, len(l)-1), ([2, 3, 4, 5, 6, 7], [1]))

        l = [3, 4, 5, 6, 7, 1, 2]
        self.assertEqual(s._split(l, 0, len(l)-1), ([3, 4, 5, 6, 7], [1, 2]))

        l = [4, 5, 6, 7, 1, 2, 3]
        self.assertEqual(s._split(l, 0, len(l)-1), ([4, 5, 6, 7], [1, 2, 3]))

        l = [5, 6, 7, 1, 2, 3, 4]
        self.assertEqual(s._split(l, 0, len(l)-1), ([5, 6, 7], [1, 2, 3, 4]))

        l = [6, 7, 1, 2, 3, 4, 5]
        self.assertEqual(s._split(l, 0, len(l)-1), ([6, 7], [1, 2, 3, 4, 5]))

        l = [7, 1, 2, 3, 4, 5, 6]
        self.assertEqual(s._split(l, 0, len(l)-1), ([7], [1, 2, 3, 4, 5, 6]))


    def test_binarySearch(self):
        s = solutions.Solution()

        target, l = 0, [1, 3]
        self.assertEqual(s._binarySearch(l, target, 0, len(l)-1), -1)

        target, l = 1, [0]
        self.assertEqual(s._binarySearch(l, target, 0, len(l)-1), -1)

        target, l = 1, [1]
        self.assertEqual(s._binarySearch(l, target, 0, len(l)-1), l.index(target))

        target, l = 1, [1, 2, 3]
        self.assertEqual(s._binarySearch(l, target, 0, len(l)-1), l.index(target))

        target, l = 2, [1, 2, 3]
        self.assertEqual(s._binarySearch(l, target, 0, len(l)-1), l.index(target))

        target, l = 3, [1, 2, 3]
        self.assertEqual(s._binarySearch(l, target, 0, len(l)-1), l.index(target))
        
        target, l = 4, [1, 2, 3]
        self.assertEqual(s._binarySearch(l, target, 0, len(l)-1),
            -1)


        target, l = 1, [1, 2, 3, 4]
        self.assertEqual(s._binarySearch(l, target, 0, len(l)), l.index(target))

        target, l = 2, [1, 2, 3, 4]
        self.assertEqual(s._binarySearch(l, target, 0, len(l)), l.index(target))

        target, l = 3, [1, 2, 3, 4]
        self.assertEqual(s._binarySearch(l, target, 0, len(l)), l.index(target))

        target, l = 4, [1, 2, 3, 4]
        self.assertEqual(s._binarySearch(l, target, 0, len(l)), l.index(target))


        
if __name__ == '__main__':
    unittest.main()
