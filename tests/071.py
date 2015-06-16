import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.071_simplify_path', fromlist='*')


class Test(unittest.TestCase):

    def test_simplifyPath(self):
        s = solutions.Solution()

        self.assertEqual(s.simplifyPath("/home/"), "/home")
        self.assertEqual(s.simplifyPath("/a/./b/../../c/"), "/c")
        self.assertEqual(s.simplifyPath("/../"), "/")
        self.assertEqual(s.simplifyPath("/home//foo/"), "/home/foo")
        self.assertEqual(s.simplifyPath("/home//foo/../."), "/home")
        self.assertEqual(s.simplifyPath("./abaw/home"), "/abaw/home")
        self.assertEqual(s.simplifyPath("./abaw/..///../"), "/")

        self.assertEqual(s.simplifyPath(""), "/")

        
        
if __name__ == '__main__':
    unittest.main()
