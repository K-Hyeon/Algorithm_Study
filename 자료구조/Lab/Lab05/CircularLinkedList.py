from Node import *

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        string_repr = ''
        if self.head is not None:
            while True:
                string_repr += str(temp) + "->"
                temp = temp.next
                if temp == self.head:
                    break
        return string_repr

    def addFront(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            self.head.next = self.head
        else:
            new_node.next = self.head.next
            self.head.next = new_node

    def addRear(self, data):
        new_node = Node(data)

        if self.head is new_node:
            self.head = new_node
            new_node.next = self.head
            self.head.next = self.head
        else:
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node

    def addAt(self, pos, data):
        if pos == self.getSize()-1:
            self.addRear(data)
            return
        if pos == 0:
            self.addFront(data)
            return

        new_node = Node(data)
        before = self.getNodeAt(pos - 1)
        if before is None:
            print("This node doesn't exist in CLL")
            return

        new_node.next = before.next
        before.next = new_node

    def deleteFront(self):
        if self.isEmpty():
            print("List is Empty...")
            return None

        temp = self.head
        if temp == temp.next:
            self.head = None
            return temp
        else:
            temp = self.head.next
            self.head.next = temp.next
            temp.next = None
            return temp

    def deleteRear(self):
        temp = self.head
        if self.isEmpty():
            print('List is Empty...')
            return None

        if self.head == self.head.next:
            self.head = None
            return temp

        else:
            before = self.getNodeAt(self.getSize()-2)
            self.head = before
            self.head.next = temp.next
            temp.next = None
            return temp

    def deleteAt(self, pos):
        temp = Node()
        if pos == self.getSize()-1:
            temp = self.deleteRear()
        elif pos == 0:
            temp = self.deleteFront()
        else:
            before = self.getNodeAt(pos - 1)
            if before is None:
                print("This node doesn't exist in DLL")
                return

            temp = before.next
            before.next = temp.next
            temp.next = None
        return temp

    def getNodeAt(self, pos):
        if (pos < 0) or (pos > self.getSize()):
            return None
        temp = self.head
        if self.head is not None:
            while True:
                temp = temp.next
                pos -= 1
                if pos < 0:
                    break
        return temp

    # print every node data
    def printList(self, msg='CircularlySingly Linked List: '):
        print(msg, end='')
        temp = self.head

        if self.head is not None:
            while True:
                print(temp, end='->')
                temp = temp.next
                if temp == self.head:
                    break
        print()

    def getDataAt(self, pos):
        pass

    def replaceDataAt(self, pos, data):
        pass

    def isEmpty(self):
        return self.head is None

    def clear(self):
        self.head = None

    def getSize(self):
        temp = self.head
        count = 0
        if self.head is not None:
            while True:
                count += 1
                temp = temp.next
                if temp == self.head:
                    break
        return count

    def findData(self, node):
        temp = self.head.next
        pos = 0
        while True:
            temp = temp.next
            pos += 1
            if (temp.data == node.data) or (pos > self.getSize()+1):
                break
        return pos % self.getSize()
