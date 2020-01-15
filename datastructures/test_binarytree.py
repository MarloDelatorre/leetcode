from unittest import main, TestCase

from binarytree import TreeNode, binarytree, to_list

class BinaryTreeTestCase(TestCase):
    def test_to_list_none(self):
        self.assertListEqual(to_list(None), [])

    def test_to_list_value(self):
        root = TreeNode(1)
        self.assertListEqual(to_list(root), [1])

    def test_to_list_missing_right(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertListEqual(to_list(root), [1, 2])

    def test_to_list_missing_left(self):
        root = TreeNode(1)
        root.right = TreeNode(2) 
        self.assertListEqual(to_list(root), [1, None, 2])

    def test_to_list_both_children(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertListEqual(to_list(root), [1, 2, 3])

    def test_to_list_left_leaves(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(5)
        self.assertListEqual(to_list(root), [1, 2, 3, 4, None, 5])

    def test_to_list_right_leaves(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertListEqual(to_list(root), [1, 2, 3, None, 4, None, 5]) 

    def test_to_list_middle_leaves(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(5)
        self.assertListEqual(to_list(root), [1, 2, 3, None, 4, 5])
    
    def test_binarytree_empty(self):
        self.assertIsNone(binarytree([]))

    def test_binarytree_values(self):
        cases = [
            [1],
            [1, 2],
            [1, None, 2],
            [1, 2],
            [1, 2, 3],
            [1, 2, 3, 4, None, 5],
            [1, 2, 3, None, 4, None, 5],
            [1, 2, 3, None, 4, 5]
        ]
        for values in cases:
            with self.subTest(values):
                self.assertListEqual(to_list(binarytree(values)), values)

if __name__ == "__main__":
    main()