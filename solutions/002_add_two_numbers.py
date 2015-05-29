class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    head = None
    cur = None
    carry = 0
    cur1 = l1
    cur2 = l2
    while cur1 or cur2:
        x = 0
        y = 0
        if cur1 != None:
            x = cur1.val
            cur1 = cur1.next
        if cur2 != None:
            y = cur2.val
            cur2 = cur2.next

        s = x + y + carry
        node = ListNode(0)
        if s >= 10:
            node.val = s % 10
            carry = int(s/10)
        else:
            node.val = s
            carry = 0

        if head == None:
            head = node
            cur = node
        else:
            cur.next = node
            cur = node

    if carry != 0:
        node = ListNode(carry)
        cur.next = node

    return head


def printList(node):
    print "list:"
    while node:
        print node.val
        node = node.next

# node1 = ListNode(8)
# head = ListNode(1)
# head.next = node1

# node2 = ListNode(0)

# result = addTwoNumbers(head, node2)
# printList(result)

a = ListNode(5)
b = ListNode(4)
c = ListNode(3)

a.next = b
b.next = c

aa = ListNode(5)
bb = ListNode(6)
cc = ListNode(4)
aa.next = bb
bb.next = cc

l1 = a
l2 = aa
result = addTwoNumbers(l1, l2)
printList(result)

