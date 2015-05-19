class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(self.getMin(), x)))

    # @return nothing
    def pop(self):
        self.stack.pop()        

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1][0]

    # @return an integer
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]


# ms = MinStack()

# print(ms.getMin())

# ms.push(1)
# ms.push(10)
# print(ms.getMin())


# ms.push(3)
# print(ms.top())
# print(ms.top())

# ms.pop()
# print(ms.top())

# ms.pop()
# print(ms.top())

# ms.pop()
# print(ms.top())
# print(ms.getMin())

# ms.push(100)
# print(ms.getMin())

# ms.push(-100)
# ms.push(-300)
# print(ms.getMin())