class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next

if __name__=='__main__':
    linkedList = LinkedList()
    second = Node(2)
    third = Node(3)

    linkedList.head = Node(0)
    linkedList.head.next = second
    second.next = third

    linkedList.printLinkedList()
