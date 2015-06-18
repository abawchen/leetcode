import unittest
import sys
sys.path.append('./')
solutions = __import__('solutions.072_edit_distance', fromlist='*')


class Test(unittest.TestCase):

    def test_minDistance(self):
        s = solutions.Solution()

        w1, w2 = "ab", "abcde"
        self.assertEqual(s.minDistance(w1, w2), 3)

        w1, w2 = "abdde", "abcde"
        self.assertEqual(s.minDistance(w1, w2), 1)


        w1, w2 = "abaw", "icela"
        self.assertEqual(s.minDistance(w1, w2), 5)
                    
        w1, w2 = "appropriate meaning", "approximate matching"
        self.assertEqual(s.minDistance(w1, w2), 7)


if __name__ == '__main__':
    unittest.main()
