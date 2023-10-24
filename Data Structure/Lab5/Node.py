class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.next = nxt

    def __str__(self):
        return "(" + str(self.data) + ")"

    def getData(self):
        return self.data

    def setData(self, d):
        self.data = d

    def getNext(self):
        return self.next

    def setNext(self, n):
        self.next = n
