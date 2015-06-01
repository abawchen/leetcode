import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.024_swap_nodes_in_pairs', fromlist='*')
helper = __import__('utils.helper', fromlist='*')



class Test024(unittest.TestCase):

    def test_swapPairs(self):
        s = solutions.Solution()

        head = helper.constructListNode([1, 2, 3, 4])
        head = s.swapPairs(head)
        self.assertEqual(
            helper.listNodeToArray(head),
            [2, 1, 4, 3]
        )
        

        head = helper.constructListNode([1])
        head = s.swapPairs(head)
        self.assertEqual(
            helper.listNodeToArray(head),
            [1]
        )


        head = helper.constructListNode([1, 2])
        head = s.swapPairs(head)
        self.assertEqual(
            helper.listNodeToArray(head),
            [2, 1]
        )


        head = helper.constructListNode([1, 2, 3])
        head = s.swapPairs(head)
        self.assertEqual(
            helper.listNodeToArray(head),
            [2, 1, 3]
        )


if __name__ == '__main__':
    unittest.main()