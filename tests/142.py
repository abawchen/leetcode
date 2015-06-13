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


if __name__ == '__main__':
    unittest.main()
