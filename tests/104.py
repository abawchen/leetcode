solution = __import__('solutions.104', fromlist='*')


def test_solution():
    s = solution.Solution()
    root = solution.TreeNode(3)
    assert s.maxDepth(root) == 1

    n1_1 = solution.TreeNode(9)
    root.left  = n1_1
    assert s.maxDepth(root) == 2

    n1_2 = solution.TreeNode(20)
    root.right = n1_2
    n2_1 = solution.TreeNode(15)
    n2_2 = solution.TreeNode(7)
    n1_2.left  = n2_1
    n1_2.right = n2_2
    assert s.maxDepth(root) == 3

    n3_1 = solution.TreeNode(31)
    n3_2 = solution.TreeNode(32)
    n2_1.left = n3_1
    n2_2.right = n3_2
    assert s.maxDepth(root) == 4

    n3_3 = solution.TreeNode(33)
    n2_2.left = n3_3
    assert s.maxDepth(root) == 4

    assert s.maxDepth(None) == 0
