# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# For example,

#     1
#    / \
#   2   3

# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.

# Return the sum = 12 + 13 = 25. 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        if not root:
            return int(0)

        path = {root:[str(root.val)]}
        stack = [root]
        l = []
        while stack:
            parent = stack.pop()
            if not parent.left and not parent.right:
                l.extend([path[parent]])
            else:
                for node in [parent.left, parent.right]:
                    if node:
                        path[node] = path[parent][:] + [str(node.val)]
                        stack.append(node)

        return int(reduce(lambda x, y: int(x) + int(y), map(lambda x: ''.join(x), l)))

s = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
# n3 = TreeNode(3)
n1.left = n2
# n1.right = n3
print s.sumNumbers(n1)

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(9)
n5 = TreeNode(3)
n6 = TreeNode(4)
n7 = TreeNode(7)
n8 = TreeNode(2)
n9 = TreeNode(1)
n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8
n6.right = n9
print s.sumNumbers(n1)