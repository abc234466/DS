class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def enqueue(self, data):
        if self.isEmpty() is True:
            print("The queue is empty")
            newNode = LinkedNode(data)
            print(f"{newNode.data} pushed into queue")
            self.front = newNode
            self.rear = self.front
            self.size += 1
            return
        newNode = LinkedNode(data)
        print(f"{newNode.data} pushed into queue")
        self.rear.next = newNode
        self.rear = newNode
        self.size += 1
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print(f"{self.front.data} popped from queue")
        tempnode = self.front
        self.front = self.front.next
        self.size -= 1
        
    def getSize(self):
        print("Total Size of queue is : ", self.size)
        return self.size

    def showqueue(self):
        temp = self.size
        tempnode = self.front
        queue = ""
        while tempnode != self.rear.next:
            queue = queue + str(tempnode.data)
            tempnode = tempnode.next
        print(queue)
    
# TEST
queue = QueueLinkedList()
queue.enqueue(3)
queue.enqueue(5)
queue.getSize()
queue.showqueue()

queue.dequeue()
queue.getSize()
queue.showqueue()            
