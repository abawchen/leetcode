# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        if root == None:
            return []

        paths = []
        stack = [root]
        dic = {root:(sum, [root.val])}
        while stack:
            node = stack.pop()
            val = dic[node][0] - node.val
            
            if val == 0 and node.left == None and node.right == None:
                paths.extend([dic[node][1]])

            self.checkAndPush(stack, dic, node, node.right, val)
            self.checkAndPush(stack, dic, node, node.left, val)
        
        return paths

    def checkAndPush(self, stack, dic, parent, node, val):
        if node:
            stack.append(node)
            path = dic[parent][1][:]
            path.append(node.val)
            dic[node] = val, path


s = Solution()

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(11)
n5 = TreeNode(13)
n6 = TreeNode(4)
n7 = TreeNode(7)
n8 = TreeNode(2)
n9 = TreeNode(5)
n10 = TreeNode(1)
n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8
n6.left = n9
n6.right = n10

print(s.pathSum(n2, 12))
print(s.pathSum(n2, 17))

print(s.pathSum(n10, 1))
print(s.pathSum(n10, 10))

n1 = TreeNode(1)
n2 = TreeNode(1)
n3 = TreeNode(1)
n4 = TreeNode(1)
n5 = TreeNode(1)
n6 = TreeNode(1)
n7 = TreeNode(1)
n8 = TreeNode(1)
n9 = TreeNode(1)
n10 = TreeNode(1)
n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8
n6.left = n9
n6.right = n10
print(s.pathSum(n1, 4))
print(s.pathSum(n1, 3))

print(s.pathSum(n10, 3))