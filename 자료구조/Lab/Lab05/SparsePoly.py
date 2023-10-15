from DoublyLinkedList import *
from Term import *

class SparsePoly(DoublyLinkedList):
    def __init__(self):
        super().__init__()

    def add(self, B):
        c = SparsePoly()
        c_expon = []

        for i in range(B.getSize()):
            for j in range(self.getSize()):
                if B.getDataAt(i).getExpon() == self.getDataAt(j).getExpon():
                    c_expon.append(B.getDataAt(i).getExpon())
                    # If the mathematical operators are the same.
                    if B.getDataAt(i).getSgn() == self.getDataAt(j).getSgn():
                        sgn = B.getDataAt(i).getSgn()
                        coeff = B.getDataAt(i).getCoeff() + self.getDataAt(j).getCoeff()
                        # Add a value to C.
                        c.addRear(Term(sgn, coeff, B.getDataAt(i).getExpon()))
                    else:
                        sgn = B.getDataAt(i).getSgn() if B.getDataAt(i).getCoeff() > self.getDataAt(
                            j).getCoeff() else self.getDataAt(j).getCoeff()
                        coeff = B.getDataAt(i).getCoeff() - self.getDataAt(j).getCoeff()
                        # Add a value to C.
                        c.addRear(Term(sgn, coeff, B.getDataAt(i).getExpon()))

        for i in range(B.getSize()):
            if B.getDataAt(i).getExpon() not in c_expon:
                # Add a value to C.
                c.addRear(Term(B.getDataAt(i).getSgn(), B.getDataAt(i).getCoeff(), B.getDataAt(i).getExpon()))

        for i in range(self.getSize()):
            if self.getDataAt(i).getExpon() not in c_expon:
                # Add a value to C.
                c.addRear(Term(self.getDataAt(i).getSgn(), self.getDataAt(i).getCoeff(), self.getDataAt(i).getExpon()))

        return c

    def sub(self, B):
        c = SparsePoly()
        c_expon = []

        for i in range(B.getSize()):
            for j in range(self.getSize()):
                if B.getDataAt(i).getExpon() == self.getDataAt(j).getExpon():
                    c_expon.append(B.getDataAt(i).getExpon())
                    # + +
                    if (B.getDataAt(i).getSgn() == '+') & (self.getDataAt(j).getSgn() == '+'):
                        sgn = '-' if B.getDataAt(i).getCoeff() > self.getDataAt(j).getCoeff() else '+'
                        coeff = self.getDataAt(j).getCoeff() - B.getDataAt(i).getCoeff()
                        # Add a value to C.
                        c.addRear(Term(sgn, abs(coeff), B.getDataAt(i).getExpon()))
                    # + -
                    elif (B.getDataAt(i).getSgn() == '+') & (self.getDataAt(j).getSgn() == '-'):
                        coeff = B.getDataAt(i).getCoeff() + self.getDataAt(j).getCoeff()
                        # Add a value to C.
                        c.addRear(Term('+', coeff, B.getDataAt(i).getExpon()))
                    # - +
                    elif (B.getDataAt(i).getSgn() == '-') & (self.getDataAt(j).getSgn() == '+'):
                        coeff = B.getDataAt(i).getCoeff() + self.getDataAt(j).getCoeff()
                        # Add a value to C.
                        c.addRear(Term('-', coeff, B.getDataAt(i).getExpon()))
                    # - -
                    elif (B.getDataAt(i).getSgn() == '-') & (self.getDataAt(j).getSgn() == '-'):
                        sgn = '+' if B.getDataAt(i).getCoeff() > self.getDataAt(j).getCoeff() else '-'
                        coeff = B.getDataAt(i).getCoeff() - self.getDataAt(j).getCoeff()
                        # Add a value to C.
                        c.addRear(Term(sgn, abs(coeff), B.getDataAt(i).getExpon()))

        for i in range(B.getSize()):
            if B.getDataAt(i).getExpon() not in c_expon:
                # Add a value to C.
                c.addRear(Term(B.getDataAt(i).getSgn(), B.getDataAt(i).getCoeff(), B.getDataAt(i).getExpon()))

        for i in range(self.getSize()):
            if self.getDataAt(i).getExpon() not in c_expon:
                # Add a value to C.
                c.addRear(Term(self.getDataAt(i).getSgn(), self.getDataAt(i).getCoeff(), self.getDataAt(i).getExpon()))

        return c

    def getDegree(self):
        best = self.getDataAt(0).getExpon()
        for i in range(1, self.getSize()):
            if self.getDataAt(i).getExpon() > best:
                best = self.getDataAt(i).getExpon()
        return best

    def display(self, msg=""):
        print("\t", msg, end='')
        node = self.head
        while node is not None:
            print(node, end='')
            node = node.getNext()
        print()

    def read(self):
        self.clear()
        while True:
            token = input("input term (syn coef  expon): ").split(" ")
            if token[0] == '-1':
                self.display("The Polynomial: ")
                return
            self.addAt(self.getSize(), Term(token[0], float(token[1]), int(token[2])))
