from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree, to_list

def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1:
        return t2
    if not t2:
        return t1

    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    t1.val += t2.val
    return t1

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            to_list(mergeTrees(
                binarytree([1, 3, 2, 5]),
                binarytree([2, 1, 3, None, 4, None, 7])
            )),
            [3, 4, 5, 5, 4, None, 7]
        )

    def test_none_plus_none(self):
        self.assertIsNone(mergeTrees(None, None))

    def test_node_plus_none(self):
        self.assertEqual(mergeTrees(TreeNode(1), None).val, 1)

    def test_none_plus_node(self):
        self.assertEqual(mergeTrees(None, TreeNode(1)).val, 1)

    def test_node_plus_node(self):
        self.assertEqual(mergeTrees(TreeNode(1), TreeNode(2)).val, 3)

    def test_left_leaf_plus_right_leaf(self):
        self.assertListEqual(
            to_list(mergeTrees(
                binarytree([1, 2]),
                binarytree([2, None, 4])
            )),
            [3, 2, 4]
        )

if __name__ == "__main__":
    main()