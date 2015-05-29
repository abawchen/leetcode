# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None or head.next == None:
            return head

        cur = head.next
        head.next = None

        while cur:
            tmp = cur.next
            cur.next = head
            head = cur
            cur = tmp

        return head


def printList(node):
    print "list:"
    while node:
        print node.val
        node = node.next

if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)

    a.next = b
    b.next = c

    s = Solution()
    head = s.reverseList(a)
    printList(head)
