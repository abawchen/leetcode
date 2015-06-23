from list_node import ListNode
from random_list_node import RandomListNode

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


def constructRandomListNode(myList):
    if not myList:
        return None

    head = RandomListNode(myList[0])
    node = head
    for v in myList[1:]:
        node.next = RandomListNode(v)
        node = node.next

    return head


def randomListNodeToArray(head):
    myList = []
    node = head
    while node:
        myList.append(node.label)
        if node.random:
            myList.append("r:"+str(node.random.label))
        node = node.next

    return myList