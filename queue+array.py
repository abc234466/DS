class Queue:
    def __init__(self, volume):
        self.front = 0
        self.size = 0
        self.rear = volume - 1
        self.queue = [None] * volume
        self.volume = volume
    def isFull(self):
        return self.size == self.volume 
    def isEmpty(self):
        return self.size == 0
    def enqueue(self, data):
        if self.isFull():
            print("The queue is full")
            return
        self.rear = (self.rear + 1) % self.volume
        self.queue[self.rear] = data
        print(f"{data} enqueued into queue")
        self.queue[self.rear] = data
        self.size += 1
    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty")
            return
        print(f"{self.queue[self.front]} dequeued from queue")
        self.front = (self.front + 1) % self.volume
        self.size -= 1
    def getfront(self):
        if self.isEmpty():
            print("The queue is empty")
            return
        return self.queue[self.front]
    def getrear(self):
        if self.isEmpty():
            print("The queue is empty")
            return
        return self.queue[self.rear]
    def showqueue(self):
        temp = self.front
        tempsize = 0
        totalqueue = ""
        while tempsize != self.size :  
            totalqueue += str(self.queue[temp % self.volume])
            tempsize += 1
            temp += 1
        print(totalqueue)
            

# TEST
if __name__ == '__main__':
    queue = Queue(10) # initialize the Queue

    
    queue.dequeue() # TEST dequeue while data is empty
    
    # enqueue
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(1)
    queue.enqueue(8)
    queue.enqueue(5)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(1)
    queue.enqueue(8)
    queue.enqueue(5)
    queue.enqueue(10)
    
    queue.showqueue() # show queue data

    # get front and rear data
    print("Front : ", queue.getfront())
    print("Rear : ", queue.getrear())
