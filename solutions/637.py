"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
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
            n = 0.0
            for node in levels[level]:
                n += node.val
                if node.left is not None:
                    levels[level+1].append(node.left)
                if node.right is not None:
                    levels[level+1].append(node.right)
            ans.append(n/len(levels[level]))
            level += 1
        return ans
