import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.042_trapping_rain_water', fromlist='*')


class Test(unittest.TestCase):

    def test_trap(self):
        s = solutions.Solution()

        height = [0, 1, 0, 2]
        self.assertEqual(s.trap(height), 1)

        height = [1, 0, 1]
        self.assertEqual(s.trap(height), 1)

        height = [0, 1, 0, 2, 1, 0, 1, 3]
        self.assertEqual(s.trap(height), 5)

        height = [0, 1, 0, 2, 1, 0, 1]
        self.assertEqual(s.trap(height), 2)

        height = [0, 1, 0, 2, 1, 0, 1, 2]
        self.assertEqual(s.trap(height), 5)

        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        height = self.assertEqual(s.trap(height), 6)

        height = [5, 2, 1, 0, 3, 0, 3, 4]
        height = self.assertEqual(s.trap(height), 15)

        height = [5, 2, 1, 0, 3]
        height = self.assertEqual(s.trap(height), 6)

        height = [0, 1, 2, 3, 2]
        self.assertEqual(s.trap(height), 0)

        height = [0, 1, 2, 3, 2, 1]
        self.assertEqual(s.trap(height), 0)

        height = [0, 1, 2, 3]
        self.assertEqual(s.trap(height), 0)

        height = [10, 0, 1, 0, 1, 0, 1, 9, 0, 5]
        self.assertEqual(s.trap(height), 56)

        height = [10, 0, 10, 0, 1, 0, 1, 0, 1, 9, 0, 5]
        self.assertEqual(s.trap(height), 66)

        height = [5, 4]
        self.assertEqual(s.trap(height), 0)


        height = [9, 6, 8, 8, 5, 6, 3]
        self.assertEqual(s.trap(height), 3)

        
if __name__ == '__main__':
    unittest.main()
