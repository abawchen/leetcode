# Given a linked list, remove the nth node from the end of list and return its head.

# For example,

#    Given linked list: 1->2->3->4->5, and n = 2.

#    After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:
# Given n will always be valid.
# Try to do this in one pass. 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):

        # no extra space
        fast = slow = head

        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next

        while fast.next:
            fast, slow = fast.next, slow.next

        slow.next = slow.next.next
        return head

        # extra space O(n)
        # if not head:
        #     return head

        # i = 0
        # dic = {}
        # node = head;
        # while node:
        #     dic[i] = node
        #     node = node.next
        #     i += 1

        # p = i - n
        # if p is 0:
        #     head = head.next
        # else:
        #     dic[p-1].next = dic.get(p+1, None)
        # return head

    def printList(self, head):
        print "==========="
        cur = head
        while cur:
            print cur.val
            cur = cur.next
        print "==========="

s = Solution()

n0 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(5)
# n5 = ListNode(6)
# n6 = ListNode(7)

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
# n4.next = n5
# n5.next = n6

# n0 = s.removeNthFromEnd(n0, 3)
# n0 = s.removeNthFromEnd(None, 0)

s.printList(n0)

