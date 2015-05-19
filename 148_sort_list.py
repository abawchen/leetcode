class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if head == None or head.next == None:
            return head

        i = 0
        dic = {}
        node = head
        while node:
            dic[i] = node
            node = node.next
            i += 1
        
        mid = i/2
        right = self.sortList(dic.get(mid, None))
        dic[mid-1].next = None
        left = self.sortList(head)
        
        return self.merge(left, right)

    def merge(self, left, right):

        node = ListNode(0)
        head = node
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        
        node.next = left if left else right

        return head.next


    def printList(self, head):
        print '--- start ---'
        while head:
            print head.val
            head = head.next
        print '---  end  ---'
        # print 'xxx'

s = Solution()

n1 = ListNode(1)
n2 = ListNode(3)
n3 = ListNode(2)
# n4 = ListNode(4)

n1.next = n2
n2.next = n3
# n3.next = n4

l = s.sortList(n1)
s.printList(l)



