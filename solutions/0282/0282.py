import unittest
from collections import defaultdict

class Solution:
    
    def compute(self, dp, start, end):
        # print((start, end))
        if start >= end:
            return {}

        if (start, end) not in dp:
            # print((start, end), self.num[start:end])
            # dp[(start, end)] = [self.num[start:end]]
            # if self.num[start] != "0":
            #     dp[(start, end)].add(self.num[start:end])
            # else:
            #     return dp[(start, end)]
            # dp[(start, end)].add(str(int(self.num[start:end])))
            # if self.num[start] == "0" and end - start > 1:
            #     # XXX: take care leading zeros
            #     print(self.num[start:end], start, end)
            #     return {}

            dp[(start, end)].add(self.num[start:end])
            # print("Abc", self.num[start:end], start, end)
            
            for i in range(start, end):
                heads = self.compute(dp, start, i+1)
                tails = self.compute(dp, i+1, end)
                print(start, i, i+1, end, heads, tails)
                for op in ["+","-","*"]:
                    # print(start, i, heads)
                    for h in heads:
                        for t in tails:
                            # print(h+op+t)
                            dp[(start, end)].add(h+op+t)
                        
        return dp[(start, end)]
    
    def addOperators(self, num: str, target: int) -> list[str]:
        dp = defaultdict(set)
        ans = []
        self.num = num
        self.compute(dp, 0, len(num))
        for v in dp[(0, len(num))]:
            print(v)
            if eval(v) == target:
                ans.append(v)

        return ans

class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    # def test_01(self):
    #     # num = "123"
    #     num = "12"
    #     target = 6
    #     # expected = ["1*2*3","1+2+3"]
    #     got = self.solution.addOperators(num, target)
    #     # self.assertEqual(sorted(expected), sorted(got))

    # def test_02(self):
    #     num = "123"
    #     target = 6
    #     expected = ["1*2*3","1+2+3"]
    #     got = self.solution.addOperators(num, target)
    #     self.assertEqual(sorted(expected), sorted(got))

    # def test_03(self):
    #     num = "105"
    #     target = 5
    #     expected = ["1*0+5","10-5"]
    #     got = self.solution.addOperators(num, target)
    #     self.assertEqual(sorted(expected), sorted(got))


    def test_04(self):
        num = "00"
        target = 0
        expected = ["0*0","0+0","0-0"]
        got = self.solution.addOperators(num, target)
        # print(got)
        self.assertEqual(sorted(expected), sorted(got))

if __name__ == '__main__':
    unittest.main()