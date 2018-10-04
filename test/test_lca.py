import unittest
from LCA.lca import LCA
from LCA.binary_tree import BinaryTree


class TestLCA(unittest.TestCase):

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

    def test_lca(self):
        self.assertEqual(5, LCA().lca(self.ten_node_tree, 3, 12).value)

        self.assertEqual(17, LCA().lca(self.ten_node_tree, 10, 85).value)

        self.assertEqual(None, LCA().lca(self.ten_node_tree, 1, 2))

        self.assertEqual(None, LCA().lca(self.empty_tree, 1, 2))

        self.assertEqual(1, LCA().lca(self.degenerative_tree, 1, 2).value)

    def tearDown(self):
        self.empty_tree = None
        self.ten_node_tree = None
        self.degenerative_tree = None

