# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if head and head.next:
            n = -1
            dic = {}
            cur = head
            while cur:
                n += 1
                dic[n] = cur
                cur = cur.next

            head.next = dic.get(n, None)
            cur = head.next
            f, b = 1, n-1
            t = True

            for i in xrange(1, n + 1):
                if t:
                    j = f
                    f += 1
                else:
                    j = b
                    b -= 1
                t = not t
                cur.next = dic[j]
                cur = cur.next
            
            dic[(n+1)/2].next = None

        self.printList(head)

    def printList(self, head):
        print "==========="
        cur = head
        while cur:
            print cur.val
            cur = cur.next

        # cur = head
        # print cur.val
        
        # cur = cur.next
        # print cur.val

        # cur = cur.next
        # print cur.val

        # cur = cur.next
        # print cur.val

        # cur = cur.next
        # print cur.val

        print "==========="


n0 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(5)
n5 = ListNode(6)
n6 = ListNode(7)

n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

s = Solution()
s.reorderList(n0)
# s.reorderList(None)