import unittest
from LCA.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.empty_tree = BinaryTree()

        self.degenerative_tree = BinaryTree()
        file = open("resources/one_child_node.txt", 'r')
        values = file.readline()
        for x in values:
            self.degenerative_tree.add(int(x))

        self.ten_node_tree = BinaryTree()
        file = open("resources/ten_node.txt", 'r')
        values = file.readline()
        for x in values:
            self.ten_node_tree.add(int(x))

    def test_get_root(self):
        root = self.empty_tree.get_root()
        self.assertEqual(root, None)

        root = self.degenerative_tree.get_root()
        self.assertEqual(root, 1)

        root = self.ten_node_tree.get_root()
        self.assertEqual(root, 5)

    def test_print_tree(self):
        self.assertEqual("tree is empty", self.empty_tree.print_tree())

    def test_add(self):

