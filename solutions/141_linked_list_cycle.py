# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space? 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False

        visited = set()
        node = head.next
        while node:
            if node in visited:
                return True

            visited.add(node)
            node = node.next

        return False