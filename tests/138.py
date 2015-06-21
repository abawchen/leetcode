import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.138_copy_list_with_random_pointer', fromlist='*')
helper = __import__('utils.helper', fromlist='*')


class Test(unittest.TestCase):

    def test_copyRandomList(self):
        s = solutions.Solution()

        head = helper.constructRandomListNode([1, 2, 3, 4])
        newHead = s.copyRandomList(head)
        self.assertEqual(helper.randomListNodeToArray(newHead),
            [1, 2, 3, 4])

        head = helper.constructRandomListNode([1, 2, 3, 4])
        head.random = head.next
        newHead = s.copyRandomList(head)
        self.assertEqual(helper.randomListNodeToArray(newHead),
            [1, 'r:2', 2, 3, 4])

        head = helper.constructRandomListNode([1, 2, 3, 4])
        head.random = head.next
        head.next.random = head
        newHead = s.copyRandomList(head)
        self.assertEqual(helper.randomListNodeToArray(newHead),
            [1, 'r:2', 2, 'r:1', 3, 4])


        head = helper.constructRandomListNode([1, 2, 3, 4])
        head.random = head.next
        head.next.random = head
        head.next.next.random = head.next
        head.next.next.next.random = head.next.next.next
        newHead = s.copyRandomList(head)
        self.assertEqual(helper.randomListNodeToArray(newHead),
            [1, 'r:2', 2, 'r:1', 3, 'r:2', 4, 'r:4'])


        newHead = s.copyRandomList(None)
        self.assertEqual(newHead, None)


        head = helper.constructRandomListNode([1])
        # head.random = head.next
        newHead = s.copyRandomList(head)
        self.assertEqual(helper.randomListNodeToArray(newHead),
            [1])


        head = helper.constructRandomListNode([1])
        head.random = head
        newHead = s.copyRandomList(head)
        self.assertEqual(helper.randomListNodeToArray(newHead),
            [1, 'r:1'])



if __name__ == '__main__':
    unittest.main()

