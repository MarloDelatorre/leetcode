from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def isBalanced(root: TreeNode) -> bool:
    if not root:
        return True

    def get_is_balanced_and_height(node: TreeNode) -> (bool, int):
        if not node:
            return (True, -1)

        is_left_bal, left_height = get_is_balanced_and_height(node.left)

        if not is_left_bal:
            return (False, left_height)

        is_right_bal, right_height = get_is_balanced_and_height(node.right)

        if not is_right_bal:
            return (False, right_height)

        node_is_balanced = abs(left_height - right_height) <= 1
        node_height = max(left_height, right_height) + 1

        return (node_is_balanced, node_height)

    is_balanced, _ = get_is_balanced_and_height(root)
    return is_balanced


class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(isBalanced(binarytree([3, 9, 20, None, None, 15, 7])))

    def test_given_case_2(self):
        self.assertFalse(isBalanced(binarytree([1, 2, 2, 3, 3, None, None, 4, 4])))

    def test_empty_tree(self):
        self.assertTrue(isBalanced(None))

    def test_single_node(self):
        self.assertTrue(isBalanced(TreeNode(1)))

if __name__ == "__main__":
    main()