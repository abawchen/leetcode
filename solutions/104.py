"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given a binary tree, find its minimum depth.

The maximum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        tree = [(root, level)]
        while len(tree) != 0:
            node, level = tree.pop(0)
            if node is None:
                continue
            level += 1
            tree.append((node.left, level))
            tree.append((node.right, level))
        return level
