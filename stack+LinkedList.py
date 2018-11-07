class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.base = None
    def isEmpty(self):
        return True if self.base == None else False
    def push(self, data):
        newNode = LinkedNode(data)
        newNode.next = self.base
        self.base = newNode
        print(f"{data} pushed into stack\n")
    def pop(self):
        if self.isEmpty():
            return float("-inf")
        popdata = self.base.data
        self.base = self.base.next
        print(f"{popdata} popped from stack\n")
        return popdata
    def peek(self):
        if self.base != None:
            print(self.base.data)
            return self.base.data
        else:
            print("Nothing in the stack\n")
            return float("-inf")
    def printStack(self):
        print("==Total itmes in the Stack==")
        temp = self.base
        while temp != None:
            print(temp.data)
            temp = temp.next
        print("== END ==")
# TEST
stack = Stack()
stack.peek()
stack.push(5)
stack.push(1)
stack.push(3)
stack.printStack()
stack.pop()
stack.peek()

            
    
