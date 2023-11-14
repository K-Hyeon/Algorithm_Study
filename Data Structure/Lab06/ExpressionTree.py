from BinaryTree import *
from queue import LifoQueue

class ExpressionTree(BinaryTree):
    def __init__(self, root = None):
        super().__init__(root)

    def isOperator(self, c):
        if (c=='+' or c=='-' or c=='*' or c=='/' or c=='^'):
            return True
        else:
            return False

    def constructTree(self, postfix):
        stack = LifoQueue()

        # Traverse through every character of input expression
        for char in postfix:
            # if operand, simply push into stack
            if not self.isOperator(char):
                t = Node(char)
                stack.put(t)
            # Operator
            else:
                # Pop tow top nodes
                t = Node(char)
                t1 = stack.get()
                t2 = stack.get()

                # make them children
                t.setRight(t1)
                t.setLeft(t2)

                # Add this subexpression to stack
                stack.put(t)

        # Only element will be the root of expression tree
        et = stack.get()

        return et
