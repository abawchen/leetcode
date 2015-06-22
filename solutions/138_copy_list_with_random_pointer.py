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
        while cur:
            newCur.random = cur.random
            cur.random = newCur

            cur = cur.next
            if cur:
                newCur.next = RandomListNode(cur.label)
                newCur = newCur.next


        newCur = newHead
        dupCur = dupHead = RandomListNode(head.label)
        while newCur:
            if newCur.random:
                dupCur.random = newCur.random
                newCur.random = newCur.random.random
            dupCur.next = RandomListNode(0)
            newCur, dupCur = newCur.next, dupCur.next

        cur, dupCur = head, dupHead
        while cur:
            cur.random = dupCur.random
            cur, dupCur = cur.next, dupCur.next

        return newHead