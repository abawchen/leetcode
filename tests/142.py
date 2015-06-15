import unittest
import sys
sys.path.append('./')
solutions = __import__('solutions.142_linked_list_cycle_ii', fromlist='*')
helper = __import__('utils.helper', fromlist='*')


class Test(unittest.TestCase):

    def test_detectCycle(self):
        s = solutions.Solution()

        head = helper.constructListNode([1, 2])
        self.assertEqual(s.detectCycle(head), None)

        head = helper.constructListNode([1, 2, 3, 4])
        self.assertEqual(s.detectCycle(head), None)

        head = helper.constructListNode([1])
        head.next = head
        self.assertEqual(s.detectCycle(head), head)

        head = helper.constructListNode([1, 2])
        head.next.next = head
        self.assertEqual(s.detectCycle(head), head)

        self.assertEqual(s.detectCycle(None), None)

        head = helper.constructListNode([1, 2, 3, 4])
        head.next.next.next = head.next
        self.assertEqual(s.detectCycle(head), head.next)



        head = helper.constructListNode([i for i in xrange(1, 22)])
        dic = self._listNodeDic(head)
        dic[21].next = dic[18]
        self.assertEqual(s.detectCycle(head), dic[18])

        dic[21].next = dic[10]
        self.assertEqual(s.detectCycle(head), dic[10])


    def _listNodeDic(self, head):
        dic = {}
        i, node = 1, head
        while node:
            dic[i], node = node, node.next
            i += 1
        return dic


if __name__ == '__main__':
    unittest.main()
