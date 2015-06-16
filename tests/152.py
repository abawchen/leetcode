import unittest
import sys
sys.path.append('./')
solutions = __import__('solutions.152_maximum_product_subarray', fromlist='*')


class Test(unittest.TestCase):

    def test_maxProduct(self):
        s = solutions.Solution()

        nums = [2, 3, -2, 4]
        self.assertEqual(s.maxProduct(nums), 6)


        nums = [2, 3, -2, 4, 5]
        self.assertEqual(s.maxProduct(nums), 20)


        nums = [2, 3, -2, 4, 5, -1]
        self.assertEqual(s.maxProduct(nums), 2*3*2*4*5)

        nums = [2, 3, -2, 4, 5, -1, -20]
        self.assertEqual(s.maxProduct(nums), 400)

        nums = [2, 3, -2, 4, 5, -1, -20, 5]
        self.assertEqual(s.maxProduct(nums), 2000)

        nums = [2, 3, -2, 4, 5, -1, -20, 5, -100]
        self.assertEqual(s.maxProduct(nums), 240*10000)


        nums = [2, 3, -2, 4, 5, -1, -20, 5, -100, 0, 1000000000]
        self.assertEqual(s.maxProduct(nums), 1000000000)

        nums = [-1, -1, -1]
        self.assertEqual(s.maxProduct(nums), 1)

        nums = [-1, 1, -1, -100]
        self.assertEqual(s.maxProduct(nums), 100)

        nums = [-1, 1, -1, -100, 0, -1, -1000]
        self.assertEqual(s.maxProduct(nums), 1000)

        nums = [-1, 1, -1, -100, 0, -1, 1000, -2, -3, 5]
        self.assertEqual(s.maxProduct(nums), 30000)

        nums = [-1, 1, -1, -100, 0, -7, 1000, -2, -3, 2]
        self.assertEqual(s.maxProduct(nums), 14000)


        nums = [-2, -1, 0]
        self.assertEqual(s.maxProduct(nums), 2)

        nums = [-2, -8, 0, -1, 3]
        self.assertEqual(s.maxProduct(nums), 16)

        nums = [-2]
        self.assertEqual(s.maxProduct(nums), -2)

        nums = [0, -3, 1 ,1]
        self.assertEqual(s.maxProduct(nums), 1)

        nums = [0, 2]
        self.assertEqual(s.maxProduct(nums), 2)

if __name__ == '__main__':
    unittest.main()
