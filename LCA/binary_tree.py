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
            return self._find(value, node.left)
        elif value > node.value and node.right is not None:
            return self._find(value, node.right)

        return None

    def tree_to_str(self):
        if self.root is not None:
            return self._tree_to_str(self.root, "")
        else:
            return "tree is empty"

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


def main():
    ten_node_tree = BinaryTree()
    file = open("../resources/ten_node_tree.txt", 'r')
    values = file.readlines()
    for x in values:
        ten_node_tree.add(int(x.strip()))
    file.close()

    print(ten_node_tree.find(12))


if __name__ == '__main__':
    main()
