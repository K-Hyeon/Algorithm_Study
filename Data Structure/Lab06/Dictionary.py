from BinarySearchTree import *
from Record import *

class Dictionary(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def searchByWord(self, word):
        pass

    def searchByMeaning(self, meaning):
        pass

    def searchMeaning(self, n, meaning):
        pass

    def runDict(self):
        wdict = Dictionary()
        while True:
            command = input('i- insert, d-delete, p-print, s-search, m-search meaning, q-quit -> ')

            if command == 'i':
                word = input(' > word: ').strip()
                meaning = input(' > meaning: ').strip()
                wdict.insert_bst(Record(word, meaning))
            elif command == 'd':
                word = input('inter word: ')
                wdict.delete_bst(Record(word, None))
                print('\n')
            elif command == 'p':
                print('Dictionary: ')
                wdict.inorder(wdict.root)
                print('\n')
            elif command == 's':
                word = input(' > word: ').strip()
                n = wdict.search(wdict.root, Record(word, None))
                if n is not None:
                    print('Record is ', n)
                else:
                    print('The: ' + word + 'is not found')
            elif command == 'q':
                return
