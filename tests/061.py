import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.061_rotate_list', fromlist='*')
helper = __import__('utils.helper', fromlist='*')


class Test(unittest.TestCase):

    def test_rotateRight(self):
        s = solutions.Solution()

        k = 10
        ln = None
        head = s.rotateRight(ln, k)
        self.assertEqual(head, None)

        k = 100
        nums = [1]
        ln = helper.constructListNode(nums)
        head = s.rotateRight(ln, k)
        self.assertEqual(helper.listNodeToArray(head), self._shift(nums, k))

        # Given  1->2->3->4->5->NULL and k = 1,
        # return 5->1->2->3->4->NULL.
        k = 1
        nums = [1, 2, 3, 4, 5]
        ln = helper.constructListNode(nums)
        head = s.rotateRight(ln, k)
        self.assertEqual(helper.listNodeToArray(head), self._shift(nums, k))

        # Given  1->2->3->4->5->NULL and k = 2,
        # return 4->5->1->2->3->NULL.
        k = 2
        ln = helper.constructListNode(nums)
        head = s.rotateRight(ln, k)
        self.assertEqual(helper.listNodeToArray(head), self._shift(nums, k))

        # Given  1->2->3->4->5->NULL and k = 3,
        # return 3->4->5->1->2->NULL.
        k = 3
        ln = helper.constructListNode(nums)
        head = s.rotateRight(ln, k)
        self.assertEqual(helper.listNodeToArray(head), self._shift(nums, k))

        # Given  1->2->3->4->5->NULL and k = 4,
        # return 2->3->4->5->1->NULL.
        k = 4
        ln = helper.constructListNode(nums)
        head = s.rotateRight(ln, k)
        self.assertEqual(helper.listNodeToArray(head), self._shift(nums, k))

        # Given  1->2->3->4->5->NULL and k = 5,
        # return 1->2->3->4->5->NULL.
        k = 5
        ln = helper.constructListNode(nums)
        head = s.rotateRight(ln, k)
        self.assertEqual(helper.listNodeToArray(head), self._shift(nums, k))

        k = 6
        ln = helper.constructListNode(nums)
        head = s.rotateRight(ln, k)
        self.assertEqual(helper.listNodeToArray(head), self._shift(nums, k))

    def _shift(self, nums, n):
        n %= len(nums)
        return nums[-n:]+nums[:-n]
        
if __name__ == '__main__':
    unittest.main()
