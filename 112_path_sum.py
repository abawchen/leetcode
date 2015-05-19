# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root == None:
            return False

        stack = [root]
        dic = {root:sum}

        while stack:
            node = stack.pop()
            val = dic[node] - node.val
            
            if val == 0 and node.left == None and node.right == None:
                return True

            self.checkAndPush(stack, dic, node.left, val)
            self.checkAndPush(stack, dic, node.right, val)
        
        return False

    def checkAndPush(self, stack, dic, node, val):
        if node:
            stack.append(node)
            dic[node] = val


s = Solution()

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(11)
n5 = TreeNode(13)
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
print 22, (s.hasPathSum(n1, 22)) # True
print 26, (s.hasPathSum(n1, 26)) # True
print 18, (s.hasPathSum(n1, 18)) # True
print 13, (s.hasPathSum(n1, 13)) # False
print 27, (s.hasPathSum(n1, 27)) # True


print 1, (s.hasPathSum(n9, 1))
print 10, (s.hasPathSum(n9, 10))
