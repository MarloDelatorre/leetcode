from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def diameterOfBinaryTree(root: TreeNode) -> int:
    longest_path = 0

    def max_path(node: TreeNode):
        if not node:
            return 0
        left_length = max_path(node.left)
        right_length = max_path(node.right)
        nonlocal longest_path
        longest_path = max(longest_path, left_length + right_length)
        return 1 + max(left_length, right_length)

    max_path(root)
    return longest_path

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(diameterOfBinaryTree(binarytree([1, 2, 3, 4, 5])), 3)

    def test_empty_tree(self):
        self.assertEqual(diameterOfBinaryTree(None), 0)

    def test_single_node(self):
        self.assertEqual(diameterOfBinaryTree(TreeNode(1)), 0)

    def test_longest_path_not_root(self):
        self.assertEqual(
            diameterOfBinaryTree(binarytree(
                [1, 2, None, 5, 3, None, None, 6, None, 7]
            )),
            4
        )

if __name__ == "__main__":
    main()