class BinaryNode:
    def __init__(self, value = None):
        """Create binary node"""
        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        """Adds a new node to the tree containing this value"""
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)

    def delete(self):
        """
        Remove value of self from BinaryTree. Works in conjunction
        with remove method in BinaryTree
        """

        if self.left is self.right is None:
            return None
        if self.left is None:
            return self.right
        if self.right is None:
            return self.left

        child = self.left
        grandchild = child.right
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = child.right
            self.value = grandchild.value
            child.right = grandchild.left
        else:
            self.left = child.left
            self.value = child.value

        return self


class BinaryTree:
    def __init__(self):
        """Create empty binary tree"""
        self.root = None

    def add(self, value):
        """Insert value into proper location in Binary Tree"""
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def contains(self, target):
        """Check whether BST contains target value"""
        node = self.root
        while node:
            if target == node.value:
                return True
            if target < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def remove(self, value):
        """Remove value from tree"""

        if self.root:
            self.root = self.remove_from_parent(self.root, value)

    def remove_from_parent(self, parent, value):
        """Remove value from tree rooted at parent"""
        if parent is None:
            return None

        if value == parent.value:
            return parent.delete()
        elif value < parent.value:
            parent.left = self.remove_from_parent(parent.left, value)
        else:
            parent.right = self.remove_from_parent(parent.right, value)

        return parent


import random
from time import time


def performance():
    """Demonstrate execution performance"""
    n = 1024
    while n <= 65536:
        bt = BinaryTree()
        now = time()
        for i in range(n):
            bt.add(random.randint(1, n))

        bt.contains(random.randint(1, n))
        print(n, (time() - now) * 1000)

        n *= 2

# performance()



