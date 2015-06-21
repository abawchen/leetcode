# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list. 


# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return

        cur = head
        newCur = newHead = RandomListNode(cur.label)

        while cur.next:
            cur = cur.next
            newCur.next = RandomListNode(cur.label)
            newCur = newCur.next

        cur, newCur = head, newHead
        while cur:
            if cur.random:
                newCur.random = cur.random
            node = cur
            cur = cur.next
            node.next = newCur
            newCur = newCur.next

        newCur = newHead
        while newCur:
            if newCur.random:
                newCur.random = newCur.random.next
            newCur = newCur.next
        
        return newHead