from SinglyLinkedList import *
from LineEditor import *
from DoublyLinkedList import *
from SparsePoly import *
from CircularLinkedList import *
from JosephusProblem import *

def testNodes():
    a = Node()
    b = Node(23, None)
    c = Node(99, b)
    d = Node(100, c)
    print(a, b, c.getNext(), c, d, d.getNext())

def testSinglyLinkedList():
    list = SinglyLinkedList()

    list.addAt(0, 10)
    list.addAt(0, 20)
    list.addAt(1, 30)
    list.addAt(list.getSize(), 40)
    list.addAt(2, 50)
    list.addFront(23)
    list.addRear(25)
    list.printList("Element in the List : ")
    print(list.getDataAt(2))
    list.replaceDataAt(2, 90)
    print("List after replacing 2nd element :", list)
    list.reverseList()
    print("List after reversing :", list)
    print(list.deleteFront())
    print("List after deleting element from front : ", list)
    print(list.deleteRear())
    print("List after deleting element from rear : ", list)
    print(list.deleteAt(2))
    print("List after deleting 2nd element : ", list)
    print(list.deleteAt(0))
    list.deleteAt(list.getSize())
    print("List after deleting 3rd element: ", list)
    list.clear()
    print(list)

def testDoublyLinkedList():
    list2 = DoublyLinkedList()
    print(list2.getSize())
    list2.addRear(30)
    list2.addRear(35)
    list2.addFront(47)
    print(list2)
    print(list2.getSize())
    list2.addFront(50)
    list2.addRear(40)
    list2.addFront(55)
    list2.addRear(60)
    list2.addAt(3, 70)
    list2.addAt(3, 80)
    print(list2)
    print("deleted -> ", list2.deleteFront())
    print("deleted -> ", list2.deleteRear())
    print("deleted -> ", list2.deleteAt(2))
    print("deleted -> ", list2.deleteAt(2))

    print(list2)

def testPoly():
    a = SparsePoly()
    b = SparsePoly()
    a.read()
    b.read()
    a.display("A = ")
    b.display("B = ")
    print("\t A degree is ", a.getDegree())
    print("\t B degree is ", b.getDegree())

    a.add(b).display("Sum = ")
    a.sub(b).display("Sub = ")

def testCircularLinkedList():
    list = CircularLinkedList()
    print(list.getSize())
    list.addFront(30)
    list.addFront(15)
    print(list)
    print(list.getSize())

    list.addFront(35)
    list.addFront(20)
    list.addFront(22)
    list.addFront(25)
    list.addFront(50)
    list.addRear(150)
    list.addRear(250)
    print(list)
    print("deleted ->",list.deleteFront())
    print(list)
    print("deleted ->", list.deleteRear())
    print(list)
    print("deleted ->", list.deleteAt(3))
    print("position ->", list.findData(list.head.next), list.head.next)
    print("position ->", list.findData(list.head), list.head)
    print(list)

def testJosephusProblem():
    jp = JosephusProblem(10, 3)
    jp.runJosephus()



def main():
    # testNodes()
    # testSinglyLinkedList()

    # test Line Editor
    #le = LineEditor()
    #le.runLineEditor()

    #testDoublyLinkedList()
    #testPoly()

    #testCircularLinkedList()
    testJosephusProblem()


if __name__ == "__main__":
    main()
