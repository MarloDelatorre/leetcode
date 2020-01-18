from typing import List
from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def binaryTreePaths(root: TreeNode) -> List[str]:
    paths = []

    if not root:
        return paths

    def build_paths(node: TreeNode, base_string: str) -> None:
        if not node.left and not node.right:
            nonlocal paths
            paths.append(base_string + str(node.val))
        base_string += str(node.val) + "->"
        if node.left:
            build_paths(node.left, base_string)
        if node.right:
            build_paths(node.right, base_string)
    build_paths(root, "")

    return paths

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(
            set(binaryTreePaths(binarytree([1, 2, 3, None, 5]))),
            set(["1->2->5", "1->3"])
        )

    def test_empty_tree(self):
        self.assertEqual(binaryTreePaths(None), [])

    def test_single_node(self):
        self.assertListEqual(binaryTreePaths(TreeNode(1)), ["1"])

    def test_full_tree(self):
        self.assertEqual(
            set(binaryTreePaths(binarytree([1, 2, 3, 4, 5, 6, 7]))),
            set(["1->2->4", "1->2->5", "1->3->6", "1->3->7"])
        )

if __name__ == "__main__":
    main()