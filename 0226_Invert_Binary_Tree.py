from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree, to_list

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root

class Test(TestCase):
    def test_given_case_1(self):
        self.assertListEqual(
            to_list(invertTree(binarytree(
                [4, 2, 7, 1, 3, 6, 9]
            ))),
            [4, 7, 2, 9, 6, 3, 1]
        )

    def test_root_is_none(self):
        self.assertIsNone(invertTree(None))

    def test_single_node(self):
        self.assertListEqual(to_list(invertTree(TreeNode(1))), [1])

    def test_right_leaf_only(self):
        self.assertListEqual(to_list(invertTree(binarytree(
            [1, None, 2]
            ))),
            [1, 2]
        )

if __name__ == "__main__":
    main()