import unittest
from LCA.lca import LCA
from LCA.binary_tree import BinaryTree


class TestLCA(unittest.TestCase):

    # initialise trees used for testing
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

    # tests for lca
    def test_lca(self):
        # testing lca in a normal binary tree where root is lca
        self.assertEqual(5, LCA().lca(self.ten_node_tree, 3, 12).value)
        # testing lca in a normal binary tree where lca is in right subtree
        self.assertEqual(17, LCA().lca(self.ten_node_tree, 10, 85).value)
        # testing lca in a normal binary tree where lca does not exist as one of the node is not present in the tree
        self.assertEqual(None, LCA().lca(self.ten_node_tree, 1, 2))
        # testing lca in an empty tree
        self.assertEqual(None, LCA().lca(self.empty_tree, 1, 2))
        # testing lca in a degenerative tree
        self.assertEqual(1, LCA().lca(self.degenerative_tree, 1, 2).value)
        # testing data structure that is not a tree
        self.assertEqual("binary tree structures is not as defined", LCA().lca(object(), 1, 2))

    # clean up
    def tearDown(self):
        self.empty_tree = None
        self.ten_node_tree = None
        self.degenerative_tree = None

