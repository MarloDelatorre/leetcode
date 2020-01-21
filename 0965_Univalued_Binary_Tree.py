from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def isUnivalTree(root: TreeNode) -> bool:
    if not root:
        return True

    def all_have_value(node: TreeNode, value: int) -> bool:
        if not node:
            return True

        return node.val == value and \
            all_have_value(node.left, value) and \
            all_have_value(node.right, value)

    return all_have_value(root, root.val)

class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(isUnivalTree(binarytree([1, 1, 1, 1, 1, None, 1])))

    def test_given_case_2(self):
        self.assertFalse(isUnivalTree(binarytree([2, 2, 2, 5, 2])))

    def test_empty_tree(self):
        self.assertTrue(isUnivalTree(None))

    def test_single_node(self):
        self.assertTrue(isUnivalTree(TreeNode(1)))

if __name__ == "__main__":
    main()
