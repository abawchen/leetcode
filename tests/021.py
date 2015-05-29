import unittest
import sys
sys.path.append('./')

# http://stackoverflow.com/questions/147507/how-does-one-do-the-equivalent-of-import-from-module-with-pythons-import
solutions = __import__('solutions.021_merge_two_sorted_lists', fromlist='*')
helper = __import__('utils.helper', fromlist='*')


class Test021(unittest.TestCase):

    def test_mergeTwoLists(self):
        s = solutions.Solution()

        head = s.mergeTwoLists(None, None)
        self.assertEqual(head, None)

        l1 = helper.constructListNode([1, 2, 3, 4])
        head = s.mergeTwoLists(l1, None)
        self.assertEqual(helper.listNodeToArray(head), [1, 2, 3, 4])

        l1 = helper.constructListNode([1, 2, 3, 4])
        head = s.mergeTwoLists(None, l1)
        self.assertEqual(helper.listNodeToArray(head), [1, 2, 3, 4])

        l1 = helper.constructListNode([1, 2, 3, 4])
        l2 = helper.constructListNode([1, 2, 3, 4])
        head = s.mergeTwoLists(l1, l2)
        self.assertEqual(helper.listNodeToArray(head), [1, 1, 2, 2, 3, 3, 4, 4])


        l1 = helper.constructListNode([1, 2, 3, 4, 5, 6, 7])
        l2 = helper.constructListNode([1, 2, 3, 4])
        head = s.mergeTwoLists(l1, l2)
        self.assertEqual(helper.listNodeToArray(head), [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7])

        l1 = helper.constructListNode([1, 2, 3, 4, 5, 6, 7])
        l2 = helper.constructListNode([1, 2, 3, 4])
        head = s.mergeTwoLists(l2, l1)
        self.assertEqual(helper.listNodeToArray(head), [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7])


        l1 = helper.constructListNode([1])
        head = s.mergeTwoLists(l1, None)
        self.assertEqual(helper.listNodeToArray(head), [1])


if __name__ == '__main__':
    unittest.main()

