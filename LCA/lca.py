# from LCA.binary_tree import BinaryTree


class LCA:

    """
    tries to find lca of two nodes in binary tree by determining whether the nodes exists in the subtrees starting at
    node. The algorithm is as follows:
    1. if root equals a then lca equals a similarly if root equals b then lca equals b, however only if the other
    node is also present in the tree
    2. if a and b are both in left subtree then lca is in left subtree
    3. if a and b are both in right subtree then lca is in right subtree
    4. if a and b are in each one of right and left subtree then the root is lca
    :parameter
    tree : root to binary tree. Binary tree structure only, however does not have protocols to identify binary trees
    therefore there will be errors if something other than a binary tree is passed in
    a : value of the first node, used to reference the representing node in binary tree
    b : value of the second node, used to reference the representing node in binary tree

    :returns
    lca : Node object that is the lca of a and b if it exists else None

    """
    def lca(self, tree, a, b):
        exists = [False, False]

        lca = self._find_lca(tree.root, a, b, exists)

        if exists[0] and exists[1] or exists[0] and tree.find(b) or exists[1] and tree.find(a):
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


"""
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
"""
