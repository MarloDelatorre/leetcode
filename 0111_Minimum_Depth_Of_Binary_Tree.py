from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def minDepth(root: TreeNode) -> int:
    def min_depth_util(node: TreeNode, level: int=0) -> int:
        if not node.left and not node.right:
            return level + 1

        level += 1
        min_left = min_depth_util(node.left, level) if node.left else float("inf")
        min_right = min_depth_util(node.right, level) if node.right else float("inf")

        return min(min_left, min_right)

    return min_depth_util(root) if root else 0

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(minDepth(binarytree([3, 9, 20, None, None, 15, 7])), 2)

    def test_empty_tree(self):
        self.assertEqual(minDepth(None), 0)

    def test_single_node(self):
        self.assertEqual(minDepth(TreeNode(1)), 1)

    def test_single_child(self):
        self.assertEqual(minDepth(binarytree([1, 2])), 2)

    def test_depth_four(self):
        self.assertEqual(minDepth(binarytree([
            3, 9, 20, 14, None, 15, 16, None, None, None, None, 17 
        ])), 3)

if __name__ == "__main__":
    main()
