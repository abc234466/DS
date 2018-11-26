class TreeNode:
    def __init__(self, data):
        self.parent = data
        self.left = None
        self.right = None
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.parent)
        if self.right != None:
            self.right.printTree()
class Tree:
    def __init__(self):
        self.root = None

            
root = Tree()
root.root = TreeNode(3)
root.root.left = TreeNode(2)
root.root.right = TreeNode(5)

root.root.printTree()


