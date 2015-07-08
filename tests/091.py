import unittest
import sys
import itertools
sys.path.append('./')

solutions = __import__('solutions.091_decode_ways', fromlist='*')


class Test046(unittest.TestCase):

    def test_numDecodings(self):
        s = solutions.Solution()

        st = ''
        self.assertEqual(s.numDecodings(st), 0)

        st = '030'
        self.assertEqual(s.numDecodings(st), 0)

        st = '261'
        self.assertEqual(s.numDecodings(st), 2)

        st = '10'
        self.assertEqual(s.numDecodings(st), 1)

        st = '12'
        self.assertEqual(s.numDecodings(st), 2)

        st = '121'
        self.assertEqual(s.numDecodings(st), 3)

        st = '1212'
        self.assertEqual(s.numDecodings(st), 5)

        st = '1234'
        self.assertEqual(s.numDecodings(st), 3)

        st = '12260'
        self.assertEqual(s.numDecodings(st), 0)

        st = '12210'
        self.assertEqual(s.numDecodings(st), 3)

        # st = '12260121212122122'
        # self.assertEqual(s.numDecodings(st), 0)

        st = '261012'
        self.assertEqual(s.numDecodings(st), 4)

if __name__ == '__main__':
    unittest.main()