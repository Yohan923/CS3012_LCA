from LCA.binary_tree import BinaryTree


class LCA:

    def lca(self, tree, a, b):
        exists = [False, False]

        lca = self._find_lca(tree.root, a, b, exists)

        if exists[0] and exists[1] or exists[0] and tree.find(a) or exists[1] and tree.find(b):
            return lca
        else:
            return None

    def _find_lca(self, root, a, b, exists):
        if root is None:
            return None

        if root.value == a:
            exists[0] = True
            return root

        if root.value == b:
            exists[1] = True
            return root

        left_node = self._find_lca(root.left, a, b, exists)
        right_node = self._find_lca(root.right, a, b, exists)

        if left_node and right_node:
            return root

        return left_node if left_node is not None else right_node


def main():
    tree = BinaryTree()
    file = open("../resources/ten_node_tree.txt", "r")
    values = file.readlines()
    for x in values:
        tree.add(int(x.strip()))
    file.close()

    a = 1
    b = 2

    lca = LCA().lca(tree, a, b)

    print("lca of " + str(a) + " and " + str(b) + " is " + str(lca.value))


if __name__ == '__main__':
    main()
