import unittest
import sys
sys.path.append('./')
solutions = __import__('solutions.169_majority_element', fromlist='*')


class Test(unittest.TestCase):

    def test_majorityElement(self):
        s = solutions.Solution()

        l = [1]
        self.assertEqual(s.majorityElement(l), 1)

        l = [1, 1]
        self.assertEqual(s.majorityElement(l), 1)

        l = [2, 1, 2]
        self.assertEqual(s.majorityElement(l), 2)

        l = [2, 1, 2, 2]
        self.assertEqual(s.majorityElement(l), 2)

        l = [3, 2, 3, 2, 2]
        self.assertEqual(s.majorityElement(l), 2)


if __name__ == '__main__':
    unittest.main()
