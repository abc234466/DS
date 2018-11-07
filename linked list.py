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
            currentNode = currentNode.next
    def findMiddle(self, leftNode, rightNode):
        '''
        ceil
        '''
        if leftNode == None:
            return None
        fstNode = leftNode
        sndNode = leftNode
        while sndNode != rightNode and sndNode.next != rightNode:
            sndNode = sndNode.next.next
            fstNode = fstNode.next
        return fstNode
        '''
        floor
        
        if leftNode == None:
            return None
        fstNode = leftNode
        sndNode = leftNode.next
        while sndNode != rightNode:
            sndNode = sndNode.next
            if sndNode != rightNode:
                fstNode = fstNode.next
                sndNode = sndNode.next
        return fstNode
        '''
    def binarysearch(self, value):
        leftNode = self.head
        rightNode = None
        while rightNode == None or rightNode != leftNode:
            currentNode = self.findMiddle(leftNode, rightNode)
            print(currentNode)
            if currentNode == None:
                return None
            elif currentNode.data == value:
                return currentNode
            elif currentNode.data < value:
                leftNode = currentNode.next
            elif currentNode.data > value:
                rightNode = currentNode
        return None
        
            
# TEST
if __name__=='__main__':
    linkedList = LinkedList()
    second = Node(3)
    third = Node(5)
    forth = Node(8)

    linkedList.head = Node(0)
    linkedList.head.next = second
    second.next = third
    third.next = forth

    linkedList.printLinkedList()
    print(linkedList.binarysearch(9))
