from sys import maxsize

class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)
        print(f"{data} pushed into stack")
        print(f"Stack = {self.stack}\n")

    def pop(self):
        if self.isEmpty():
            print(f"Nothing in the stack")
            return
        popdata = self.stack[-1]
        self.stack = self.stack[:len(self.stack)-1]
        print(f"{popdata} popped from stack")
        print(f"Stack = {self.stack}\n")

stack = Stack()
stack.pop()
stack.push(5)
stack.push(1)
stack.push(3)
stack.push(3)
stack.pop()
           
