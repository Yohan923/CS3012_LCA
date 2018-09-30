import unittest
import io
import sys

from LCA.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.empty_tree = BinaryTree()

        self.degenerative_tree = BinaryTree()
        file = open("../resources/one_child_node.txt", 'r')
        values = file.readlines()
        for x in values:
            self.degenerative_tree.add(int(x.strip()))
        file.close()

        self.ten_node_tree = BinaryTree()
        file = open("../resources/ten_node_tree.txt", 'r')
        values = file.readlines()
        for x in values:
                self.ten_node_tree.add(int(x.strip()))
        file.close()

    def test_get_root(self):
        root = self.empty_tree.get_root()
        self.assertEqual(None, root)

        root = self.degenerative_tree.get_root()
        self.assertEqual(1, root.value)

        root = self.ten_node_tree.get_root()
        self.assertEqual(5, root.value)

    def test_print_tree(self):
        self.ten_node_tree.print_tree()
