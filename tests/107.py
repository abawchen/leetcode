solution = __import__('solutions.107', fromlist='*')


def test_solution():
    s = solution.Solution()
    root = solution.TreeNode(3)
    n1_1 = solution.TreeNode(9)
    n1_2 = solution.TreeNode(20)
    root.left  = n1_1
    root.right = n1_2
    n2_1 = solution.TreeNode(15)
    n2_2 = solution.TreeNode(7)
    n1_2.left  = n2_1
    n1_2.right = n2_2
    assert s.levelOrderBottom(root) == [[15,7],[9,20],[3]]
    assert s.levelOrderBottom(n1_1) == [[9]]
    assert s.levelOrderBottom(n1_2) == [[15,7],[20]]

    n3_1 = solution.TreeNode(31)
    n3_2 = solution.TreeNode(32)
    n2_1.left = n3_1
    n2_2.right = n3_2
    assert s.levelOrderBottom(root) == [[31,32],[15,7],[9,20],[3]]

    n3_3 = solution.TreeNode(33)
    n2_2.left = n3_3
    assert s.levelOrderBottom(root) == [[31,33,32],[15,7],[9,20],[3]]

    assert s.levelOrderBottom(None) == []
