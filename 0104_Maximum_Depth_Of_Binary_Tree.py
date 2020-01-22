from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1 + max(left_depth, right_depth)

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(maxDepth(binarytree([3, 9, 20, None, None, 15, 7])), 3)

    def test_empty_tree(self):
        self.assertEqual(maxDepth(None), 0)

    def test_single_node(self):
        self.assertEqual(maxDepth(TreeNode(3)), 1)

if __name__ == "__main__":
    main()