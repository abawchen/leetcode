import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.025_reverse_nodes_in_k_group', fromlist='*')
helper = __import__('utils.helper', fromlist='*')



class Test024(unittest.TestCase):

    def test_reverseKGroup(self):
        s = solutions.Solution()

        head = helper.constructListNode([1, 2, 3, 4])
        head = s.reverseKGroup(head, 2)
        self.assertEqual(
            helper.listNodeToArray(head),
            [2, 1, 4, 3]
        )
        

        head = helper.constructListNode([1])
        head = s.reverseKGroup(head, 2)
        self.assertEqual(
            helper.listNodeToArray(head),
            [1]
        )


        head = helper.constructListNode([1, 2])
        head = s.reverseKGroup(head, 2)
        self.assertEqual(
            helper.listNodeToArray(head),
            [2, 1]
        )


        head = helper.constructListNode([1, 2, 3])
        head = s.reverseKGroup(head, 2)
        self.assertEqual(
            helper.listNodeToArray(head),
            [2, 1, 3]
        )


        head = helper.constructListNode([1, 2, 3, 4])
        head = s.reverseKGroup(head, 3)
        self.assertEqual(
            helper.listNodeToArray(head),
            [3, 2, 1, 4]
        )

        head = helper.constructListNode([1, 2, 3, 4, 5, 6])
        head = s.reverseKGroup(head, 3)
        self.assertEqual(
            helper.listNodeToArray(head),
            [3, 2, 1, 6, 5, 4]
        )

        head = helper.constructListNode([1, 2, 3, 4, 5, 6, 7, 8])
        head = s.reverseKGroup(head, 3)
        self.assertEqual(
            helper.listNodeToArray(head),
            [3, 2, 1, 6, 5, 4, 7, 8]
        )



        head = helper.constructListNode([1, 2, 3, 4, 5, 6, 7, 8])
        head = s.reverseKGroup(head, 4)
        self.assertEqual(
            helper.listNodeToArray(head),
            [4, 3, 2, 1, 8, 7, 6, 5]
        )

        head = helper.constructListNode([1, 2, 3, 4, 5, 6, 7, 8, 9])
        head = s.reverseKGroup(head, 4)
        self.assertEqual(
            helper.listNodeToArray(head),
            [4, 3, 2, 1, 8, 7, 6, 5, 9]
        )

if __name__ == '__main__':
    unittest.main()