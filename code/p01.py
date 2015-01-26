#!/usr/bin/env python
"""convert the binary search tree to double linked queue"""
class Node:
    def __init__(self,value):
        print "A Node ",str(value)," created"
        self.value = value
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        print "a binary search tree created!"
        self.root = None

    def add_node(self,node):
        if self.root is None:
            print "root is empty"
            self.root = node
        else:
            self.__add_node_aux(self.root, node)
        return

    def __add_node_aux(self,root, node):
        if node.value > root.value:
            if root.right == None:
                root.right = node
                return
            else:
                self.__add_node_aux(root.right, node)
        else:
            if root.left == None:
                root.left = node
                return
            else:
                self.__add_node_aux(root.left, node)

    def print_post_order(self):
        self.__print_post_order_aux(self.root)

    def __print_post_order_aux(self,root):
        if root is None:
            return
        if root.left is not None:
            self.__print_post_order_aux(root.left)
        print root.value,
        if root.right is not None:
            self.__print_post_order_aux(root.right)

class DLinkQueue:
    def __init__(self):
        print "Double Link Queue created"
        self.head = None
        self.tail = None

    def set_queue(self, bsTree):
        if bsTree.root is None:
            print "BS tree is empty!"
            return
        self.__set_queue_aux(bsTree.root)

    def __set_queue_aux(self, root):
        if root.left is not None:
            self.__set_queue_aux(root.left)
        self.add_node_to_tail(root)
        if root.right is not None:
            self.__set_queue_aux(root.right)

    def add_node_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else: 
            node.left = self.tail
            self.tail.right = node
            self.tail = node
    
    def print_queue(self):
        current = self.head
        print current.value,
        while current.right is not None:
            current = current.right
            print current.value,

if __name__ == '__main__':
    n1 = Node(4)
    n2 = Node(8)
    n3 = Node(12)
    n4 = Node(16)
    n5 = Node(6)
    n6 = Node(14)
    n7 = Node(10)
    bstree = BSTree()
    bstree.add_node(n7)
    bstree.add_node(n6)
    bstree.add_node(n5)
    bstree.add_node(n4)
    bstree.add_node(n3)
    bstree.add_node(n2)
    bstree.add_node(n1)
    bstree.print_post_order()
    print " "
    dque = DLinkQueue()
    dque.set_queue(bstree)
    dque.print_queue()
