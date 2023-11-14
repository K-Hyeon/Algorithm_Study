from BinaryTree import *
from MorseCodes import *
from BinarySearchTree import *
from ExpressionTree import *
from Dictionary import *
from MinHeap import *
from Huffman import *

def useBN():
    root = Node(14)
    n2 = Node(4)
    n3 = Node(15)
    n4 = Node(3)
    n5 = Node(9)
    n6 = Node(18)
    n7 = Node(7)
    n8 = Node(16)
    n9 = Node(20)
    n10 = Node(5)
    n11 = Node(17)
    print(root, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11)

    root.setLeft(n2)
    root.setRight(n3)
    # root.left = n2
    # root.right = n3
    n2.setLeft(n4)
    n2.setRight(n5)
    n3.setRight(n6)
    n5.setLeft(n7)
    n6.setLeft(n8)
    n6.setRight(n9)
    n7.setLeft(n10)
    n8.setRight(n11)

    print(root)
    print(root.getLeft(), n2)
    print(root.getRight(), n3)

    print(root.getLeft().getLeft(), n4)
    print(root.getRight().getRight(), n6)

    # BinaryTree
    bt = BinaryTree()
    bt.setRoot(root)

    bt.printInorder()
    bt.printPreorder()
    print("Pre-order2 ", end='')
    bt.preorder2(bt.getRoot())
    print("Post-order ", end='')
    bt.printPostorder()
    print("Level-order ", end='')
    bt.levelorder(bt.getRoot())
    print("\n")
    print("count node: ", bt.countNode(bt.getRoot()))
    print("count leaf: ", bt.countLeaf(bt.getRoot()))
    print("get height: ", bt.calcHeight(bt.getRoot()))
    print("get levels: ", bt.get_levels(bt.getRoot()))

def useMorse():
    tree = MorseCodes()
    tree.makeMorseTree()
    tree.printMorseTree()

    #bt = BinaryTree(morse.root)

    print('\n[char to morse code]')
    text = 'SOS'
    encode = tree.encode(text)
    print('Encoded: ', encode)

    print('\n[morse code to char]')
    morse = ['....', '..']
    decode = tree.decode(morse)
    print('Decoded: ', decode)


def useBST():
    tree = BinarySearchTree()

    print('\n1. Test BinarySearchTree')
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]

    print('Tree for data ' + str(data))
    for i in data:
        tree.insert_bst(i)
        tree.printInorder()

    print()
    tree.printPreorder()
    tree.printPostorder()
    tree.printLevelorder()

    print('\n[tree\'s info]')
    print('Node = %d' % tree.countNode(tree.root))
    print('Leaf Nodes = %d' % tree.countLeaf(tree.root))
    print('Height = %d' % tree.calcHeight(tree.root))
    print('Maximum = %d' % tree.search_max_bst(tree.root).data)
    print('Minimum = %d' % tree.search_min_bst(tree.root).data)

    print('\n[Search Tree]')
    tree.search_bst(26)
    tree.search_bst(25)

    print('\n[Test Delete]')
    tree.printLevelorder("original: LevelOrder: ")
    tree.delete_bst(3)
    tree.printLevelorder("case1: < 3> : LevelOrder: ")
    tree.delete_bst(68)
    tree.printLevelorder("case2: <68> : LevelOrder: ")
    tree.delete_bst(18)
    tree.printLevelorder("case3: <18> : LevelOrder: ")
    tree.delete_bst(35)
    tree.printLevelorder("case4: <35> root : LevelOrder: ")

    print('\n[tree\'s info]')
    print('Node = %d' % tree.countNode(tree.root))
    print('Leaf Nodes = %d' % tree.countLeaf(tree.root))
    print('Height = %d' % tree.calcHeight(tree.root))
    print('Maximum = %d' % tree.search_max_bst(tree.root).data)
    print('Minimum = %d' % tree.search_min_bst(tree.root).data)


def useET():
    # test1,
    et = ExpressionTree()
    postfix = "ab+ef*g*-"
    tnode = et.constructTree(postfix)
    # Inorder
    print('\nInorder (infix)')
    et.inorder(tnode)
    # Preorder
    print('\nPreorder (prefix)')
    et.preorder(tnode)
    # Postorder
    print('\nPostorder (postfix)')
    et.postorder(tnode)

    # test2
    pf2 = '359++2*'
    tn = et.constructTree(pf2)
    # Inorder
    print()
    print('\nInorder (infix)')
    et.inorder(tn)
    # Preorder
    print('\nPreorder (prefix)')
    et.preorder(tn)
    # Postorder
    print('\nPostorder (postfix)')
    et.postorder(tn)
    # setRoot
    et.setRoot(tn)
    #print(et.evaluateExpressionTree())

def useDictionary():
    wmd = Dictionary()
    wmd.runDict()

def useMinHeap():
    print('\nHeap Test')
    heap = MinHeap()
    data = [2, 5, 4, 8, 9, 3, 7, 3]
    print("Data elements: " + str(data))

    for elem in data:
        heap.insert(elem)
    heap.printHeap()
    print(heap)

    heap.delete()
    heap.printHeap()

    heap.delete()
    heap.printHeap()

def useHuffman():
    #text = "hello"

    with open('test.txt') as txt_file:
        text = txt_file.read()

    hc = Huffman(text)
    hc.printCodes()

"""
def useBtree():
    btree = BTree(3)
    keys = [70, 80, 90, 10, 20, 30, 40, 50, 100]
    for key in keys:
        btree.insert(key)
        btree.display()

    key = 20
    result = btree.search
    if key:
        print(f"\n Fountd {key}")
    else:
        print(f"\nNot Fountd {key}")

    btree.delete(30)
    print("After deleting 30")
    btree.display()
"""

def main():
    print("Lab 06")
    # useBN()
    # useBST()
    # useET()
    # useDictionary()
    # useMorse()
    # useMinHeap()
    useHuffman()


if __name__ == "__main__":
    main()
