import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.031_next_permutation', fromlist='*')


class Test031(unittest.TestCase):

    def test_nextPermutation(self):
        s = solutions.Solution()

        l = [1, 3, 2]
        self.assertEqual(s.nextPermutation(l), [2, 1, 3])


        l = [1, 2, 3]
        self.assertEqual(s.nextPermutation(l), [1, 3, 2])


        l = [1, 1, 5]
        self.assertEqual(s.nextPermutation(l), [1, 5, 1])


        l = [1, 1, 2, 2]
        self.assertEqual(s.nextPermutation(l), [1, 2, 1, 2])

        l = [1, 4, 3, 2]
        self.assertEqual(s.nextPermutation(l), [2, 1, 3, 4])

        l = [1, 1]
        self.assertEqual(s.nextPermutation(l), [1, 1])

        l = [1]
        self.assertEqual(s.nextPermutation(l), [1])

        l = []
        self.assertEqual(s.nextPermutation(l), None)

        l = [6, 5, 10, 4, 3, 2]
        self.assertEqual(s.nextPermutation(l), [6, 10, 2, 3, 4, 5])


        l = [11, 6, 10, 10, 4, 3, 2]
        self.assertEqual(s.nextPermutation(l), [11, 10, 2, 3, 4, 6, 10])

        l = [11, 6, 10, 10, 4, 3, 2]
        self.assertEqual(s.nextPermutation(l), [11, 10, 2, 3, 4, 6, 10])


        l = [11, 9, 10, 10, 4, 3, 2]
        self.assertEqual(s.nextPermutation(l), [11, 10, 2, 3, 4, 9, 10])

if __name__ == '__main__':
    unittest.main()