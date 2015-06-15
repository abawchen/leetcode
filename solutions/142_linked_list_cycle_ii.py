# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Follow up:
# Can you solve it without using extra space? 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head:
            return None

        count = length = 0
        walker = runner = head
        while runner and runner.next:
            count += 1
            walker = walker.next
            runner = runner.next.next

            if walker == runner:
                if length == 0:
                    length = count
                else:
                    length = count - length
                    break

        if length == 0:
            return None

        walker = runner = head
        for _ in range(length):
            runner = runner.next

        while walker != runner:
            walker, runner = walker.next, runner.next

        return walker


        # visited = set()

        # node = head
        # while node:
        #     if node in visited:
        #         return node

        #     visited.add(node)
        #     node = node.next

        # return None