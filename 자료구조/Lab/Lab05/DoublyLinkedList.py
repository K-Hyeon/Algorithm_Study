from Node2 import *

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # String representation
    def __str__(self):
        tmp = self.head
        string_repr = ""
        while tmp:
            string_repr += str(tmp) + "->"
            tmp = tmp.next

        return string_repr + "END"

    def addFront(self, data):
        new_node = Node2(None, data, None)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node

    def addRear(self, data):
        new_node = Node2(None, data, None)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def addAt(self, pos, data):
        if pos == self.getSize():
            self.addRear(data)
            return
        if pos == 0:
            self.addFront(data)
            return

        new_node = Node2(None, data, None)
        before = self.getNodeAt(pos - 1)
        if before is None:
            print("This node doesn't exist in DLL")
            return

        new_node.next = before.next
        before.next = new_node
        new_node.prev = before
        if new_node.next is not None:
            new_node.next.prev = new_node

    # delete from head
    def deleteFront(self):
        if self.isEmpty():
            print("List is Empty..")
            return None

        temp = self.head
        if temp.next is temp.prev:  # there is just one node
            self.head = None
            return temp
        else:
            self.head = temp.next
            self.head.prev = None
            return temp

    # delete from tail
    def deleteRear(self):
        if self.isEmpty():
            print("List is Empty..")
            return None

        temp = self.head
        if temp.next is temp.prev:  # there is just one node
            self.head = None
            return temp
        else:
            while temp.next:
                temp = temp.next

            temp.prev.next = None
            temp.prev = None
            return temp

    def deleteAt(self, pos):
        temp = Node2()
        if pos == self.getSize():
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
            temp.next.prev = before
            temp.next = None
            temp.prev = None
        return temp

    def getNodeAt(self, pos):
        if (pos < 0) or (pos > self.getSize()):
            print("Invalid position")
            return None
        temp = self.head
        while pos > 0 and temp is not None:
            temp = temp.next
            pos -= 1
        return temp

    def getDataAt(self, pos):
        node = self.getNodeAt(pos)
        if node is None:
            return None
        else:
            return node.data

    def replaceDataAt(self, pos, data):
        node = self.getNodeAt(pos)
        if node is not None:
            node.data = data

    def isEmpty(self) -> bool:
        # return True if head is none
        return self.head is None

    def clear(self):
        self.head = None

    def getSize(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.getNext()
            count += 1
        return count

    def findData(self, val):
        node = self.head
        while node is not None:
            if node.data == val:
                return node
            node = node.next
        return node
