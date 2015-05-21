class LRUCache:

    class ListNode:
        def __init__(self, key, prev=None, next=None):
            self.key = key
            self.prev = prev
            self.next = next

    # @param capacity, an integer
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.nodeDic = {}
        self.valueDic = {}
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if self.capacity <= 1:
            return self.valueDic.get(key, -1)

        node = self.nodeDic.get(key, None)
        if not node:
            return -1

        if node != self.tail:
            if node != self.head:
                node.prev.next = node.next
                node.next.prev = node.prev
            else:
                node.next.prev = None
                self.head = node.next
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        return self.valueDic[key]

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.capacity <= 0:
            return

        if self.capacity == 1:
            self.valueDic.clear()
            self.valueDic[key] = value
            return

        if self.valueDic.has_key(key):
            self.valueDic[key] = value
            self.get(key)
        else:
            if len(self.valueDic) == self.capacity:
                self._removeHead()
        
            node = LRUCache.ListNode(key)
            if self.tail:
                node.prev = self.tail
                self.tail.next = node
            else:
                self.head = node
            self.tail = node
            self.nodeDic[key] = node
            self.valueDic[key] = value

    def _removeHead(self):
        node = self.head
        self.head = node.next
        self.head.prev = None
        self.nodeDic.pop(node.key)
        self.valueDic.pop(node.key)
        if len(self.valueDic) == 0:
            self.tail = None

    def printValueDic(self):
        print self.valueDic

    def printList(self):
        print "======== List ========"
        node = self.head
        while node:
            print node.key
            node = node.next
        print "======== Reversed ========"
        node = self.tail
        while node:
            print node.key
            node = node.prev
        print "======== End ========"

s = LRUCache(4)
print s.get(1) # -1

s.set(1, 10)
s.set(2, 20)
s.set(3, 30)
s.set(4, 40)
print "A", s.get(1) # 10

s.set(5, 50)
print "B", s.get(1) # 10
print "C", s.get(2) # -1
print "D", s.get(3) # 30
s.set(6, 60)
print "E", s.get(4) # -1
s.set(1, 100)
print s.get(1)
print s.get(6)
print s.get(4)
print s.get(3)
print s.get(5)
# s.printValueDic()
# s.printList()


# s = LRUCache(2)
# s.set(2,1)
# s.set(1,1)
# print s.get(2)
# s.set(4,1)
# print s.get(1)
# print s.get(2)
# [1, -1, 1]

# s = LRUCache(2)
# s.set(2,1)
# s.set(2,2)
# print s.get(2)
# s.set(1,1)
# s.set(4,1)
# print s.get(2)
# [2, -1]

# s = LRUCache(2)
# print s.get(2)
# s.set(2,6)
# print s.get(1)
# s.set(1,5)
# s.set(1,2)
# print s.get(1)
# print s.get(2)
# [-1, -1, 2, 6]



# s = LRUCache(1)
# s.set(2,1)
# print s.get(2)
# s.set(3,2)
# print s.get(2)
# print s.get(3)
# [1, -1, 2]