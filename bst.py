#!/usr/bin/env python3
# This is the implementation of the binary search tree ADT


class Node:
    """Creates a class Node object that holds data and points to the right/left children and parent Nodes."""
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

class BinarySearchTree:
    """Creates binary search tree class object, that contains several Nodes."""
    def __init__(self):
        self._root = None

    def insert(self, data):
        """Inserts a new Node."""
        if self._root is None:
            # If this is the first Node.
            self._root = Node(data, None)
            # If this is not the first node, call insert_node.
        else:
            self.insert_node(data, self._root)

    def insert_node(self, data, node):
        """Handles insertion of Nodes, when an existing root Node is in place."""
        # look at left subtree
        if data < node.data:    # If new data is less than previous Node data.
            if node.leftChild:  # If Node exists.
                self.insert_node(data, node.leftChild)
            else:               # If no previous Node.
                node.leftChild = Node(data, node)
        # look at right subtree
        else:                   # If new data is greater than previous Node data.
            if node.rightChild: # If Node exists.
                self.insert_node(data, node.rightChild)
            else:               # If no previous Node.
                node.rightChild = Node(data, node)

    def traverse(self):
        """Traverses through binary search tree, using in order traversal."""
        if self._root:
            self.traverse_in_order(self._root)

    def traverse_in_order(self, node):
        """docstring"""
        if node.leftChild:
            self.traverse_in_order(node.leftChild)

        print('%s' % node.data)

        if node.rightChild:
            self.traverse_in_order(node.rightChild)


    def get_max_value(self):
        """Recrusive helper function to start get_max()."""
        if self._root:
            return self.get_max(self._root)

    def get_max(self, node):
        """Recursively searches each right child of right tree, until last Node is reached.
        Returns data from final Node. """
        if node.rightChild:
            return self.get_max(node.rightChild)

        return node.data


    def get_min_value(self):
        """Recursive helpr function to start get_min()."""
        if self._root:
            return self.get_min(self._root)

    def get_min(self, node):
        """Recursively searches each left child of the left tree, until the last Node is reached.
        Returns data contained in the final Node."""
        if node.leftChild:
            return self.get_min(node.leftChild)

        return node.data


    def remove_node(self, data, node):
        """docstring"""
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.leftChild)

        elif data > node.data:
            self.remove_node(data, node.rightChild)
        else:

            if node.leftChild is None and node.rightChild is None:
                print("Removing a leaf node...%d" % node.data)

                parent = node.parent

                if parent and parent.leftChild == node:
                    parent.leftChild = None
                if parent and parent.rightChild == node:
                    parent.rightChild = None

                if parent is None:
                    self._root = None

                del node

            elif node.leftChild is None and node.rightChild:
                print("Removing a node with a single right child...%d" % node.data)

                parent = node.parent

                if parent:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                else:
                    self._root = node.rightChild

                node.rightChild.parent = parent
                del node

            elif node.rightChild is None and node.leftChild:
                print("Removing a node with a single left child...%d" % node.data)

                parent = node.parent

                if parent:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                else:
                    self._root = node.leftChild

                node.leftChild.parent = parent
                del node

            else:
                print("Removing node with two children...%d" % node.data)

                predecessor = self.get_predecessor(node.leftChild)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)


    def get_predecessor(self, node):
        """Returns the predecessor."""
        if node.rightChild:
            return self.get_predecessor(node.rightChild)

        return node

b = BinarySearchTree()
b.insert(1)
b.insert(-3)
b.insert(45)
b.insert(1111)
b.insert(-30)
b.insert(99)
b.insert(-100)
b.insert(1222)

b.traverse()

print('The max item is: %d' % b.get_max(b._root))

print('The min item is: %d' % b.get_min(b._root))
