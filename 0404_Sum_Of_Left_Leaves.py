from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def sumOfLeftLeaves(root: TreeNode) -> int:
    if not root:
        return 0
    left_leaf_sum = 0

    def visit(node: TreeNode, is_left: bool) -> None:
        if not node.left and not node.right:
            if is_left:
                nonlocal left_leaf_sum
                left_leaf_sum += node.val
            return

        if node.left:
            visit(node.left, True)
        if node.right:
            visit(node.right, False)

    visit(root, False)
    return left_leaf_sum

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(
            sumOfLeftLeaves(binarytree([3, 9, 20, None, None, 15, 17])),
            24
        )

    def test_empty_tree(self):
        self.assertEqual(sumOfLeftLeaves(None), 0)

    def test_single_node(self):
        self.assertEqual(sumOfLeftLeaves(TreeNode(4)), 0)

if __name__ == "__main__":
    main()
