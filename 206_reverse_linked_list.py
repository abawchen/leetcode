# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @param {ListNode} head
# @return {ListNode}
def reverseList(head):
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

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)

a.next = b
b.next = c

head = reverseList(a)
printList(head)



