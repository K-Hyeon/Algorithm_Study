from MinHeap import *
from HNode import *


class Huffman:
    def __init__(self, txt=None):
        self.text = txt
        self.mh = MinHeap()
        self.codes = {}
        self.decodes = {}

    def makeCodes(self):
        root = self.makeHuffmanTree()
        current_code = ""
        self.make_codes(root, current_code)

    def make_codes(self, root, current_code):
        if root is None:
            return
        if root.char is not None:
            self.codes[root.char] = current_code
            self.decodes[current_code] = root.char

        self.make_codes(root.left, current_code + "0")
        self.make_codes(root.right, current_code + "1")

    def makeHeap(self):
        frequencies = self.makeFrequencyDict()
        for key in frequencies:
            node = HNode(key, frequencies[key])
            self.mh.insert(node)

    def makeFrequencyDict(self):
        frequencies = {}
        for c in self.text:
            if c in frequencies:
                pass
            else:
                frequencies[c] = 0
            frequencies[c] += 1
        return frequencies

    def makeHuffmanTree(self):
        self.makeHeap()
        while self.mh.getSize() > 1:
            p = self.mh.delete()
            q = self.mh.delete()
            r = HNode(None, p.freq + q.freq, p, q)
            self.mh.insert(r)
        return self.mh.delete()

    def getEncodeText(self, text):
        encoded_text = ""
        for character in text:
            encoded_text += self.codes[character]
            return encoded_text

    def printCodes(self):
        self.makeCodes()
        for key in self.codes:
            print("{} : {}".format(key, self.codes[key]))

        print("Reverse Coding")
        for key in self.decodes:
            print("{} : {}".format(key, self.decodes[key]))
