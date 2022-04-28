import unittest
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def generate(self, dp: {}, start: int, end: int):
        if start > end:
            return [None]
        if start == end:
            dp[(start, end)] = [TreeNode(start)]

        if (start, end) not in dp:
            for i in range(start, end+1):
                lefts = self.generate(dp, start, i-1)
                rights = self.generate(dp, i+1, end)
                for left in lefts:
                    for right in rights:
                        dp[(start, end)].append(TreeNode(i, left, right))
        return dp[(start, end)]

    def generateTrees(self, n: int) -> int:
        dp = defaultdict(list)
        self.generate(dp, 1, n)
        return dp[(1, n)]



class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def traversal(self, trees):
        # left -> root -> right
        def inorder(node: TreeNode):
            if node is None:
                return

            if node.left:
                inorder(node.left)
            print(node.val)

            if node.right:
                inorder(node.right)

        for root in trees:
            print(root.val, root.left, root.right)
            inorder(root)

    def test_01(self):
        n = 1
        got = self.solution.generateTrees(n)
        print("n:", n, "len:", len(got))

    def test_02(self):
        n = 2
        got = self.solution.generateTrees(n)
        print("n:", n, "len:", len(got))

    def test_03(self):
        n = 3
        got = self.solution.generateTrees(n)
        print("n:", n, "len:", len(got))

if __name__ == '__main__':
    unittest.main()