from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def hasPathSum(root: TreeNode, k: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == k

    k -= root.val
    left = hasPathSum(root.left, k) if root.left else False
    right = hasPathSum(root.right, k) if root.right else False

    return left or right

class Test(TestCase):
    def test_given_case(self):
        self.assertTrue(
            hasPathSum(
                binarytree([
                    5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1
                ]),
                22
            )
        )

    def test_general_bad_case(self):
        self.assertFalse(
            hasPathSum(
                binarytree([
                    5, 4, 8, 1, None, 13, 4, 7, 2, None, None, None, 1
                ]),
                22
            )
        )

    def test_empty_tree_with_sum(self):
        self.assertFalse(hasPathSum(None, 22))

    def test_empty_tree_no_sum(self):
        self.assertFalse(hasPathSum(None, 0))

    def test_single_node_with_sum(self):
        self.assertTrue(hasPathSum(TreeNode(1), 1))

    def test_single_node_no_sum(self):
        self.assertFalse(hasPathSum(TreeNode(1), 22))

if __name__ == "__main__":
    main()