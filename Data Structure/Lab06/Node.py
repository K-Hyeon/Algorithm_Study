class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setData(self, data):
        self.data = data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data

    def __gt__(self, other):
        return self.data > other.data

    def __lt__(self, other):
        return self.data < other.data

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data
