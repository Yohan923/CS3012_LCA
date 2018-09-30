class BinaryTree:

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

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

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            self._find(value, node.left)
        elif value > node.value and node.right is not None:
            self._find(value, node.right)

        return None

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
        else:
            print("tree is empty")

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(str(node.value) + ' ', end='')
            self._print_tree(node.right)
            print('')


class Node:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value
