from BinaryTree import *

# BinarySearchTree
class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def search_bst(self, key):
        n = self.search(self.getRoot(), key)
        if n is not None:
            print("Item found: " + str(n.data))
        else:
            print("Item not found")

    def search(self, n, key):
        if n is None:
            return None
        elif key == n.getData():
            return n
        elif key < n.getData():
            return self.search(n.getLeft(), key)
        else:
            return self.search(n.getRight(), key)

    def insert_bst(self, key):
        n = Node(key, None, None)
        if super().isEmpty():
            self.root = n
        else:
            self.insert(self.root, n)

    def insert(self, r, n):
        if n < r:
            if r.getLeft() is None:
                r.setLeft(n)
                return True
            else:
                self.insert(r.getLeft(), n)
        elif n > r:
            if r.getRight() is None:
                r.setRight(n)
                return True
            else:
                self.insert(r.getRight(), n)
        else:
            return False

    def delete_bst(self, key):
        if not super().isEmpty():
            parent = None
            node = self.root
            while node is not None and node.getData() != key:
                parent = node
                if key < node.data:
                    node = node.left
                else:
                    node = node.right

            if node is None:
                return None

            # case by case
            if node.left is None and node.right is None:
                self.delete_bst_case1(parent, node)
            elif node.left is None or node.right is None:
                self.delete_bst_case2(parent, node)
            else:
                self.delete_bst_case3(node)

    def delete_bst_case1(self, parent, node):
        if parent is None:
            return None
        else:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None

    def delete_bst_case2(self, parent, node):
        if node.left is not None:
            child = node.left
        else:
            child = node.right

        if node == self.root:
            self.root = child
        else:
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child

    def delete_bst_case3(self, node):
        succp = node
        succ = node.right
        while succ.left is not None:
            succp = succ
            succ = succ.left

        if succp.left == succ:
            succp.left = succ.right
        else:
            succp.right = succ.right

        node.setData(succ.getData())
        node = succ

    def search_max_bst(self, n):
        while n is not None and n.right is not None:
            n = n.right
        return n

    def search_min_bst(self, n):
        while n is not None and n.left is not None:
            n = n.left
        return n
