#!/usr/bin/env python
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        print "A tree created"
        self.root = None
        self.path = []

    def insert_node(self,node):
        if self.root is None:
            self.root = node
        else:
            self.insertNodeAux(self.root,node)

    def insertNodeAux(self,root,node):
        if node.value < root.value:
            if root.left is None:
                root.left = node
            else:
                self.insertNodeAux(root.left,node)
        else:
            if root.right is None:
                root.right = node
            else:
                self.insertNodeAux(root.right,node)

    def print_post_order(self):
        self.printPostOrder(self.root)

    def print_mid_order(self):
        self.printMidOrder(self.root)

    def printPostOrder(self,root):
        if root.left is not None:
            self.printPostOrder(root.left)
        print root.value,
        if root.right is not None:
            self.printPostOrder(root.right)

    def printMidOrder(self,root):
        print root.value,
        if root.left is not None:
            self.printMidOrder(root.left)
        if root.right is not None:
            self.printMidOrder(root.right)

    def find_path(self, value):
        the_path = []
        self.findPath(self.root,value,0.0, the_path)
        return the_path

    def findPath(self, root, value, currentSum, the_path):
        newSum = currentSum + root.value
        the_path.append(root.value)
        #print "the_path has: "+ str(the_path)
        if newSum < value:
            if root.left is not None:
                self.findPath(root.left, value, newSum, the_path)
            if root.right is not None:
                self.findPath(root.right, value, newSum, the_path)
        if newSum == value:
            print "we found one path!"
            self.path.append(list(the_path))
        the_path.pop()


tree = Tree()
tree.insert_node(Node(10))
tree.insert_node(Node(5))
tree.insert_node(Node(12))
tree.insert_node(Node(4))
tree.insert_node(Node(7))
tree.print_post_order()
print ""
tree.print_mid_order()
print ""
tree.find_path(22)
print tree.path
