import unittest
from collections import defaultdict

class Solution:
    
    def calcuate(self, op, a, b):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            return int(a/b)
    
    def compute(self, dp, start, end):
        if start > end:
            return

        if (start, end) not in dp:
            if self.expression[start:end].isdigit():
                dp[(start, end)] = [int(self.expression[start:end])]
            else:
                for i in range(start, end):
                    if self.expression[i] in {"+","-","*","/"}:
                        heads = self.compute(dp, start, i)
                        tails = self.compute(dp, i+1, end)
                        for h in heads:
                            for t in tails:
                                dp[(start, end)].append(self.calcuate(self.expression[i], h, t))
                        
        return dp[(start, end)]
    
    def diffWaysToCompute(self, expression: str) -> list[int]:
        dp = defaultdict(list)
        self.expression = expression
        self.compute(dp, 0, len(expression))
        return dp[(0, len(expression))]



class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()


    def test_01(self):
        expression = "2-1-1"
        expected = [0,2]
        got = self.solution.diffWaysToCompute(expression)
        self.assertEqual(sorted(expected), sorted(got))

    def test_02(self):
        expression = "2*3-4*5"
        expected = [-34,-14,-10,-10,10]
        got = self.solution.diffWaysToCompute(expression)
        self.assertEqual(sorted(expected), sorted(got))



if __name__ == '__main__':
    unittest.main()