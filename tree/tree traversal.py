class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.lchild is None:
                    self.lchild = Node(data)
                else:
                    self.lchild.insert(data)
            elif data > self.data:
                if self.rchild is None:
                    self.rchild = Node(data)
                else:
                    self.rchild.insert(data)
        else:
            self.data = data


    def preorderTraversal(self, root):
        if root:
            print(root.data)
            self.preorderTraversal(root.lchild)
            self.preorderTraversal(root.rchild)

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.lchild)
            print(root.data)
            self.inorderTraversal(root.rchild)

    def postorderTraversal(self, root):
        if root:
            self.postorderTraversal(root.lchild)
            self.postorderTraversal(root.rchild)
            print(root.data)

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.postorderTraversal(root)
