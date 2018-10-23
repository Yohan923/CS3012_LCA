class BinaryTree:

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, value):
        if self.root is not None:
            self._add(value, self.root)
        else:
            self.root = Node(value)

    # recursively add node into tree
    def _add(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)
        else:
            return None

    # recursively find node in tree
    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self._find(value, node.left)
        elif value > node.value and node.right is not None:
            return self._find(value, node.right)

        return None

    def tree_to_str(self):
        if self.root is not None:
            return self._tree_to_str(self.root, "")
        else:
            return "tree is empty"

    # recursively generate string  representing the tree in pretty printing starting with root
    # each line contains exactly one node with chile nodes ordered left first
    def _tree_to_str(self, node, prefix):
        if node is not None:
            tree = prefix + "-" + str(node.value) + "\n"
            tree = tree + self._tree_to_str(node.left, prefix + " |")
            tree = tree + self._tree_to_str(node.right, prefix + "  ")
            return tree
        else:
            return prefix + "-None" + "\n"


class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
