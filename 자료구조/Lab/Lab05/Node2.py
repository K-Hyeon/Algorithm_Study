class Node2:
    def __init__(self, prev=None, data=None, nxt=None):
        self.prev = prev
        self.data = data
        self.next = nxt

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, d):
        self.data = d

    def setNext(self, n):
        self.next = n

    def setPrev(self, p):
        self.prev = p