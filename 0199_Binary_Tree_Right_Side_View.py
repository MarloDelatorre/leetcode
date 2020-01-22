from typing import List
from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def rightSideView(root: TreeNode) -> List[int]:
    view = []

    def make_view(node: TreeNode, level: int):
        nonlocal view
        if not node:
            return

        if level > len(view):
            view.append(node.val)

        level += 1
        make_view(node.right, level)
        make_view(node.left, level)

    make_view(root, level=1)
    return view

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            rightSideView(binarytree([1, 2, 3, None, 5, None, 4])),
            [1, 3, 4]
        )

    def test_empty_tree(self):
        self.assertEqual(rightSideView(None), [])

    def test_single_node(self):
        self.assertListEqual(rightSideView(TreeNode(1)), [1])

    def test_left_is_deep(self):
        self.assertListEqual(
            rightSideView(binarytree([1, 2, 3, None, 4, None, None, None, 5])),
            [1, 3, 4, 5]
        )

if __name__ == "__main__":
    main()