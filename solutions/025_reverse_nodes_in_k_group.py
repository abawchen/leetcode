# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# You may not alter the values in the nodes, only nodes itself may be changed.

# Only constant memory is allowed.

# For example,
# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5 


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head:
            return None

        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        for i in xrange(k-1, len(nodes), k):
            nodes[i-(k-1):i+1] = reversed(nodes[i-(k-1):i+1])


        for i in xrange(len(nodes)-1):
            nodes[i].next = nodes[i+1]

        nodes[len(nodes)-1].next = None

        return nodes[0]