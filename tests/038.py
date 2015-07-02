import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.038_count_and_say', fromlist='*')


class Test(unittest.TestCase):

    def test_countAndSay(self):
        s = solutions.Solution()

        self.assertEquals(s.countAndSay(1), "1")
        self.assertEquals(s.countAndSay(2), "11")
        self.assertEquals(s.countAndSay(3), "21")
        self.assertEquals(s.countAndSay(4), "1211")
        self.assertEquals(s.countAndSay(5), "111221")
        self.assertEquals(s.countAndSay(6), "312211")
        self.assertEquals(s.countAndSay(7), "13112221")
        self.assertEquals(s.countAndSay(11), "11131221133112132113212221")


if __name__ == '__main__':
    unittest.main()
