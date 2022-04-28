import unittest
import operator

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = {"+","-","*","/"}
        for c in tokens:
            if c in ops:
                b, a = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(a+b)
                if c == "-":
                    stack.append(a-b)
                if c == "*":
                    stack.append(a*b)
                if c == "/":
                    stack.append(int(a/b))
            else:
                stack.append(int(c))
        return stack.pop()


class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
    
    # def test_01(self):
    #     tokens = ["2","1","+","3","*"]
    #     got = self.solution.evalRPN(tokens)
    #     expected = 9
    #     self.assertEqual(expected, got)

    def test_02(self):
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        got = self.solution.evalRPN(tokens)
        expected = 22
        self.assertEqual(expected, got)


if __name__ == '__main__':
    unittest.main()