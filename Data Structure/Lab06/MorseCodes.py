from BinarySearchTree import *

# BinarySearchTree
class MorseCodes(BinaryTree):
    def __init__(self):
        super().__init__()
        """
        self.codes = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                      'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                      'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                      '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                      '6': '-....', '7': '--...', '8': '---..', '9': '---.', '0': '-----'
        }
        """
        self.codes = {
            'E': '.', 'T': '-', 'I': '..', 'A': '.-', 'N': '-.', 'M': '--', 'S': '...', 'U': '..-', 'R': '.-.',
            'W': '.--', 'D': '-..', 'K': '-.-', 'G': '--.', 'O': '---', 'H': '....', 'V': '...-', 'F': '..-.',
            'L': '.-..', 'P': '.--.', 'J': '.---', 'B': '-...', 'X': '-..-', 'C': '-.-.', 'Y': '-.--', 'Z': '--..',
            'Q': '--.-', '5': '.....', '4': '....-', '3': '...--', '2': '..---', '1': '.----',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
        }

    def makeMorseTree(self):
        self.root = Node(None, None, None)
        for key in self.codes:
            code = self.codes[key]
            node = self.root
            for c in code:
                if c == '.':
                    if node.left is None:
                        node.left = Node(None, None, None)
                    node = node.left
                elif c == '-':
                    if node.right is None:
                        node.right = Node(None, None, None)
                    node = node.right
            node.data = key

    def printMorseTree(self):
        self.printInorder()
        self.printPreorder()
        self.printPostorder()
        self.printLevelorder()

    # morse > char
    def decode(self, code_lst):
        text = ''
        for code in code_lst:
            node = self.root
            for c in code:
                if c == '.':
                    node = node.left
                elif c == "-":
                    node = node.right
            text = text + node.data
        return text

    # chat > morse
    def encode(self, ch):
        code_lst = []
        for c in ch:
            code = self.codes[c]
            code_lst.append(code)
        return code_lst
