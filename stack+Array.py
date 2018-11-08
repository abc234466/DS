# from sys import maxsize

class Stack:
    def __init__(self):
        self.stack = []
        self.minstack = []
        self.min = float('inf')

    def isEmpty(self):
        return len(self.stack) == 0

    def getMin(self):
        print("Min Value in stack : ", self.minstack[-1], "\n")
        return self.min
    def push(self, data):
        if data < self.min :
            self.min = data
        self.stack.append(data)
        self.minstack.append(self.min)
        print(f"{data} pushed into stack")
        print(f"Stack = {self.stack}\n")

    def pop(self):
        if self.isEmpty():
            print(f"Nothing in the stack\n")
            return
        popdata = self.stack[-1]
        self.stack = self.stack[:-1]
        self.minstack = self.minstack[:-1]
        print(f"{popdata} popped from stack")
        print(f"Stack = {self.stack}\n")

# TEDT
stack = Stack()
stack.pop()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.getMin()
stack.pop()
stack.getMin()
