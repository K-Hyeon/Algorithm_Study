from Lab03 import Stack, StackApp

def useStack():
    odd = Stack()
    even = Stack()
    print('Even Stack: ', even)
    print('Odd Stack: ', odd)

    for i in range(10):
        if i%2 == 0:
            even.push(i)
        else:
            odd.push(i)

    print('Even Stack: ',even)
    print('Odd Stack: ', odd)

    # Outputs the size of the stack.
    print(odd.size())
    print(len(odd))

    # Outputs by subtracting elements from the stack one by one.
    print('Popping elements from Odd Stack:')
    while not odd.isEmpty():
        print(odd.pop())


def useStackApp():
    sa = StackApp()
    sa.convertBase(126)

    # checkBrackets
    expr = '[sds]'
    print('Are brackets are Balanced? ',sa.checkBrackets(expr))

    # Infix2Postfix
    # expr1 = '(A+B)*C'
    expr1 = '2+(4+3*2+1)/3'
    print("Postfix Expression = ", sa.Infix2Postfix(expr1)) # answer: 2432*+1+3/+

    # evalPostfix
    expr2 = '2432*+1+3/+'
    print("Postfix Evaluation = {:.2f} ".format(sa.evalPostfix(expr2))) # answer: 2.2727272727272725


def main():
    #useStack()
    useStackApp()


if __name__ == '__main__':
    main()
