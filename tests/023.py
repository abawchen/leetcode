import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.023_merge_k_sorted_lists', fromlist='*')
helper = __import__('utils.helper', fromlist='*')


class Test021(unittest.TestCase):

    def test_sortListsHead(self):
        s = solutions.Solution()

        l1 = helper.constructListNode([1, 2, 3, 4])
        l2 = helper.constructListNode([60, 400])
        l3 = helper.constructListNode([40, 400])
        nodes = s.sortListsHead([l1, l2, l3])
        self.assertEqual(
            [1, 40, 60],
            [ node.val for node in nodes ])

        nodes = s.sortListsHead([l2, l1, l3])
        self.assertEqual(
            [1, 40, 60],
            [ node.val for node in nodes ])

        nodes = s.sortListsHead([l3, l2, l1])
        self.assertEqual(
            [1, 40, 60],
            [ node.val for node in nodes ])


    def test_mergeKLists(self):
        s = solutions.Solution()

        l1 = helper.constructListNode([1, 2, 3, 4])
        l2 = helper.constructListNode([60, 400])
        head = s.mergeKLists([l1, l2])
        self.assertEqual(helper.listNodeToArray(head), [1, 2, 3, 4, 60, 400])

        l1 = helper.constructListNode([1, 2, 3, 4])
        l2 = helper.constructListNode([60, 400])
        l3 = helper.constructListNode([40, 400])
        head = s.mergeKLists([l1, l2, l3])
        self.assertEqual(helper.listNodeToArray(head), [1, 2, 3, 4, 40, 60, 400, 400])


        l1 = helper.constructListNode([1, 2, 3, 4])
        l2 = helper.constructListNode([60, 400])
        l3 = helper.constructListNode([40, 400])
        head = s.mergeKLists([l3, l2, l1])
        self.assertEqual(helper.listNodeToArray(head), [1, 2, 3, 4, 40, 60, 400, 400])


        l1 = helper.constructListNode([3])
        l2 = helper.constructListNode([60])
        l3 = helper.constructListNode([4])
        head = s.mergeKLists([l3, l2, l1])
        self.assertEqual(helper.listNodeToArray(head), [3, 4, 60])


        l1 = helper.constructListNode([3, 4, 5, 6 ,7])
        head = s.mergeKLists([l1])
        self.assertEqual(helper.listNodeToArray(head), [3, 4, 5, 6 ,7])

        l1 = helper.constructListNode([3, 4, 5, 6 ,7])
        l2 = helper.constructListNode([1, 9, 19])
        head = s.mergeKLists([l1, l2])
        self.assertEqual(helper.listNodeToArray(head), [1, 3, 4, 5, 6 ,7, 9, 19])


        l1 = helper.constructListNode([3, 4, 5, 6 ,7])
        l2 = None
        head = s.mergeKLists([l1, l2])
        self.assertEqual(helper.listNodeToArray(head), [3, 4, 5, 6 ,7])


if __name__ == '__main__':
    unittest.main()