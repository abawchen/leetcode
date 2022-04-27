class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    # inorder: left -> root -> right

    # non-recursive version
    # def inorderTraversal(self, root):
    #     if not root:
    #         return []

    #     l = []
    #     stack = [root]
    #     while stack:
    #         node = stack[-1]

    #         if node.right:
    #             stack.append(node.right)
    #             node.right = None
            
    #         else:
    #             stack.pop()
    #             l.insert(0, node.val)

    #             if node.left:
    #                 stack.append(node.left)

    #     return l

    # recursive version
    def inorderTraversal(self, root):
        if not root:
            return []

        ans = []
        def inorder(ans, node):
            if node.left:
                inorder(ans, node.left)
            ans.append(node.val)
            if node.right:
                inorder(ans, node.right)
        inorder(ans, root)
        return ans



s = Solution()

# http://datastructuresnotes.blogspot.tw/2009/02/binary-tree-traversal-preorder-inorder.html
n1 = TreeNode(7)
n2 = TreeNode(1)
n3 = TreeNode(0)
n4 = TreeNode(3)
n5 = TreeNode(2)
n6 = TreeNode(5)
n7 = TreeNode(4)
n8 = TreeNode(6)
n9 = TreeNode(9)
n10 = TreeNode(8)
n11 = TreeNode(10)

n1.left = n2
n2.left = n3
n2.right = n4
n4.left = n5
n4.right = n6
n6.left = n7
n6.right = n8

n1.right = n9
n9.left = n10
n9.right = n11

print(s.inorderTraversal(n1))


# na = TreeNode(1)
# nb = TreeNode(2)
# nc = TreeNode(3)
# na.right = nb
# nb.left = nc
# print s.inorderTraversal(na)
# print s.inorderTraversal(nc)