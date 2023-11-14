from Node import *
from queue import Queue, LifoQueue

class BinaryTree:
    def __init__(self, r=None):
        self.root = r

    def setRoot(self, node):
        self.root = node

    def getRoot(self):
        return self.root

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    def clear(self):
        self.root = None

    def printInorder(self, msg='In-order '):
        #print()
        print(msg, end='')
        self.inorder(self.getRoot())
        print()

    def inorder(self, n):
        if n is not None:
            self.inorder(n.getLeft())
            print(n, end=' ')
            self.inorder(n.getRight())

    def printPreorder(self, msg='Pre-order '):
        # print()
        print(msg, end='')
        self.preorder(self.getRoot())
        print()

    def preorder(self, n):
        if n is not None:
            print(n, end=' ')
            self.inorder(n.getLeft())
            self.inorder(n.getRight())

    def printPostorder(self, msg='Post-order '):
        #print()
        print(msg, end='')
        self.postorder(self.getRoot())
        print()

    def postorder(self, n):
        if n is not None:
            self.inorder(n.getLeft())
            self.inorder(n.getRight())
            print(n, end=' ')

    # BFS
    def printLevelorder(self, msg='Level-order '):
        #print()
        print(msg, end='')
        self.levelorder(self.getRoot())
        print()

    def levelorder(self, n):
        queue = Queue()
        queue.put(n)
        while not queue.empty():
            n1 = queue.get()
            if n1 is not None:
                print(n1, end=' ')
                queue.put(n1.getLeft())
                queue.put(n1.getRight())

    def preorder2(self, n):
        s = LifoQueue()
        s.put(n)
        while not s.empty():
            n1 = s.get()
            if n1 is not None:
                print(n1, end=' ')
                s.put(n1.getRight())
                s.put(n1.getLeft())

    def calcHeight(self, n):
        if n is None:
            return -1
        hleft = self.calcHeight(n.getLeft())
        hright = self.calcHeight(n.getRight())
        if hleft > hright:
            return hleft + 1
        else:
            return hright + 1

    def countLeaf(self, n):
        if n is None:
            return 0
        elif self.isLeaf(n):
            return 1
        else:
            return self.countLeaf(n.getLeft()) + self.countLeaf(n.getRight())

    def countNode(self, n):
        if n is None:
            return 0
        else:
            return 1 + self.countNode(n.getLeft()) + self.countNode(n.getRight())
            # return 1 + self.count_node(n.left) + self.count_node(n.right)

    def isLeaf(self, n):
        return (n.getLeft() is None) and (n.getRight() is None)

    def get_levels(self, n):
        if n is None:
            return -1
        hleft = self.get_levels(n.getLeft())
        hright = self.get_levels(n.getRight())
        if hleft > hright:
            return hleft + 1
        else:
            return hright + 1
