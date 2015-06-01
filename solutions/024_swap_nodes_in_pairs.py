# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head:
            return None

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        for i in xrange(1, len(nodes), 2):
            nodes[i-1], nodes[i] = nodes[i], nodes[i-1]


        for i in xrange(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        nodes[len(nodes)-1].next = None

        return nodes[0]

