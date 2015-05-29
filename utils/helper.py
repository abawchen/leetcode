from list_node import ListNode

def constructListNode(myList):
    if not myList:
        return None

    head = ListNode(myList[0])
    node = head
    for v in myList[1:]:
        node.next = ListNode(v)
        node = node.next

    return head


def listNodeToArray(head):
    myList = []
    node = head
    while node:
        myList.append(node.val)
        node = node.next

    return myList