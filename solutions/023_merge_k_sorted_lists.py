# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity. 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}

    def mergeKLists(self, lists):
        nodes = self.sortListsHead(lists)

        head = cur = ListNode(0)
        while nodes:
            picked = nodes[0]
            del nodes[0]
            if picked and picked.next and len(nodes):
                nodes = self.addNodeIntoSortedList(nodes, picked.next)
            cur.next = picked
            cur = cur.next

        return head.next


    def sortListsHead(self, lists):
        lists = filter(lambda l: l is not None, lists)
        nodes = [n for n in lists]
        nodes.sort(lambda n1, n2: n1.val - n2.val)
        return nodes

    def addNodeIntoSortedList(self, nodes, node):
        i = 0
        while i < len(nodes):
            if node.val <= nodes[i].val:
                break
            i += 1

        nodes.insert(i, node)
        return nodes
