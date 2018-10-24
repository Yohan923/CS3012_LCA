import unittest

from LCA.binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.empty_tree = BinaryTree()

        self.degenerative_tree = BinaryTree()
        file = open("../resources/one_child_tree.txt", 'r')
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

    # can be used to test add()
    def test_tree_to_str(self):
        self.assertEqual("-5\n" +
                         " |-1\n" +
                         " | |-None\n" +
                         " |  -3\n" +
                         " |   |-None\n" +
                         " |    -None\n" +
                         "  -17\n" +
                         "   |-12\n" +
                         "   | |-7\n" +
                         "   | | |-None\n" +
                         "   | |  -10\n" +
                         "   | |   |-None\n" +
                         "   | |    -None\n" +
                         "   |  -None\n" +
                         "    -85\n" +
                         "     |-56\n" +
                         "     | |-45\n" +
                         "     | | |-None\n" +
                         "     | |  -None\n" +
                         "     |  -None\n" +
                         "      -None\n"
                         , self.ten_node_tree.tree_to_str())

        self.assertEqual("-1\n" +
                         " |-None\n" +
                         "  -2\n" +
                         "   |-None\n" +
                         "    -3\n" +
                         "     |-None\n" +
                         "      -4\n" +
                         "       |-None\n" +
                         "        -5\n" +
                         "         |-None\n" +
                         "          -6\n" +
                         "           |-None\n" +
                         "            -None\n"
                         , self.degenerative_tree.tree_to_str())

        self.assertEqual("tree is empty", self.empty_tree.tree_to_str())

    def test_find(self):
        self.assertEqual(None, self.empty_tree.find(12))

        self.assertEqual(12, self.ten_node_tree.find(12).value)

        self.assertEqual(None, self.ten_node_tree.find(2))

    def tearDown(self):
        self.empty_tree = None
        self.ten_node_tree = None
        self.degenerative_tree = None
