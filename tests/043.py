import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.043_multiply_strings', fromlist='*')


class Test(unittest.TestCase):

    def test_multiply(self):
        s = solutions.Solution()

        num1, num2 = "1", "1"
        self.assertEqual(s.multiply(num1, num2), str(int(num1)*int(num2)))

        num1, num2 = "9", "9"
        self.assertEqual(s.multiply(num1, num2), str(int(num1)*int(num2)))

        num1, num2 = "100", "100"
        self.assertEqual(s.multiply(num1, num2), str(int(num1)*int(num2)))


        num1, num2 = "999", "9"
        self.assertEqual(s.multiply(num1, num2), str(int(num1)*int(num2)))


        num1, num2 = "999", "99"
        self.assertEqual(s.multiply(num1, num2), str(int(num1)*int(num2)))

        num1, num2 = "99", "999999999998"
        self.assertEqual(s.multiply(num1, num2), str(int(num1)*int(num2)))


        num1, num2 = "9133", "0"
        self.assertEqual(s.multiply(num1, num2), str(int(num1)*int(num2)))
        
        
        
if __name__ == '__main__':
    unittest.main()
