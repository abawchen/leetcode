import unittest
import sys
sys.path.append('./')
solutions = __import__('solutions.141_linked_list_cycle', fromlist='*')
helper = __import__('utils.helper', fromlist='*')


class Test(unittest.TestCase):

    def test_hasCycle(self):
        s = solutions.Solution()

        head = helper.constructListNode([1, 2])
        self.assertEqual(s.hasCycle(head), False)

        head = helper.constructListNode([1, 2, 3, 4])
        self.assertEqual(s.hasCycle(head), False)

        head = helper.constructListNode([1])
        head.next = head
        self.assertEqual(s.hasCycle(head), True)

        head = helper.constructListNode([1, 2])
        head.next.next = head
        self.assertEqual(s.hasCycle(head), True)

        self.assertEqual(s.hasCycle(None), False)

        head = helper.constructListNode([1, 2, 3, 4])
        head.next.next.next = head.next
        self.assertEqual(s.hasCycle(head), True)


if __name__ == '__main__':
    unittest.main()
