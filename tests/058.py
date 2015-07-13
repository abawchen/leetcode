import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.058_length_of_last_word', fromlist='*')


class Test(unittest.TestCase):


    def test_lengthOfLastWord(self):

        s = solutions.Solution()

        st = "Hello World"
        self.assertEqual(s.lengthOfLastWord(st), 5)


        st = "Hello Worl"
        self.assertEqual(s.lengthOfLastWord(st), 4)


        st = "Hello     Worl  a"
        self.assertEqual(s.lengthOfLastWord(st), 1)


        st = " Hello     Worl  a fafe ffe"
        self.assertEqual(s.lengthOfLastWord(st), 3)

        st = " a "
        self.assertEqual(s.lengthOfLastWord(st), 1)

        st = " ab "
        self.assertEqual(s.lengthOfLastWord(st), 2)


        st = " ab cdef    "
        self.assertEqual(s.lengthOfLastWord(st), 4)

        st = ""
        self.assertEqual(s.lengthOfLastWord(st), 0)


if __name__ == '__main__':
    unittest.main()
