"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        from collections import defaultdict
        level = 0
        levels = defaultdict(list)
        levels[0] = [root]
        ans = []
        while len(levels[level]) != 0:
            tmp = []
            for node in levels[level]:
                tmp.append(node.val)
                if node.left is not None:
                    levels[level+1].append(node.left)
                if node.right is not None:
                    levels[level+1].append(node.right)
            ans.append(tmp)
            level += 1
        return ans
