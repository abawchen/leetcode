# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        count = 0
        fast = slow = head
        while fast:
            fast = fast.next
            count += 1

        if k%count == 0:
            return head

        fast = head
        for i in range(k%count):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        fast.next = head
        head = slow.next
        slow.next = None

        return head