from Node import *


class SinglyLinkedList:
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
        # create a new node
        new_node = Node(data)
        if self.head:
            new_node.next = self.head  # Link new_node to head
        self.head = new_node  # make NewNode as head

    def addRear(self, data):
        if self.head is None:
            self.addFront(data)  # if this is first node, call insert_head
        else:
            temp = self.head
            while temp.next:  # traverse to Last node
                temp = temp.next
            temp.next = Node(data, None)  # create node & link to tail

    def addAt(self, pos, data):
        before = self.getNodeAt(pos - 1)
        if before is None:  # if it is the Last node.
            self.head = Node(data, self.head)
        else:
            node = Node(data, before.next)
            before.next = node

    # delete from head
    def deleteFront(self):
        tmp = self.head
        if self.head:
            self.head = self.head.next
            tmp.next = None
        return tmp

    # delete from tail
    def deleteRear(self):
        tmp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while tmp.next.next:
                    tmp = tmp.next
                second_last = tmp
                tmp = tmp.next
                second_last.next = None
        return tmp

    def deleteAt(self, pos):
        tmp = Node()
        if (self.isEmpty()) or (pos > self.getSize()):
            tmp = None
        elif pos == 0:
            tmp = self.deleteFront()
        elif pos == self.getSize():
            tmp = self.deleteRear()
        else:
            prev = self.getNodeAt(pos - 1)
            tmp = prev.next
            prev.next = tmp.next
            tmp.next = None
        return tmp

    def getNodeAt(self, pos):
        if pos < 0: return None
        node = self.head
        while (pos > 0) and (node is not None):
            node = node.next
            pos -= 1
        return node

    # print every node data
    def printList(self, msg='Singly Linked List: '):
        print(msg, end='')
        tmp = self.head
        while tmp:
            print(tmp.data, end='->')
            tmp = tmp.next
        print('END')

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

    def reverseList(self):
        prev = None
        tmp = self.head

        while tmp:
            next_node = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = next_node

        self.head = prev

    def find_Data(self, val):
        node = self.head
        while node is not None:
            if node.data == val:
                return node
            node = node.next
        return node

    def printByLine(self):
        print('Line Editor')
        node = self.head
        line = 0
        while node is not None:
            print("{} = {}".format(line, node))
            node = node.next
            line += 1
        print()
