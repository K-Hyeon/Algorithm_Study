from CircularLinkedList import *

class JosephusProblem:
    def __init__(self, n=10, m=3):
        self.list = CircularLinkedList()
        self.n = n
        self.m = m
        for i in range(1, n+1):
            self.list.addFront(i)

    def runJosephus(self):
        print(self.list)
        temp = self.list.head.next
        count = 0
        while True:
            temp = temp.next
            count += 1

            if count == self.m:
                temp2 = temp.next
                pos = self.list.findData(temp)
                print("Eliminated ->", self.list.deleteAt(pos))
                temp = temp2
                print(self.list)
                count = 0

            if temp == temp.next:
                print("Selected ->", temp)
                break
