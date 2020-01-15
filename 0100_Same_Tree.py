from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True

    if not p or not q:
        return False

    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

class Test(TestCase):
    def test_both_none(self):
        self.assertTrue(isSameTree(None, None))

    def test_one_none_other_not(self):
        self.assertFalse(isSameTree(None, TreeNode(1)))

    def test_same_single_value(self):
        self.assertTrue(isSameTree(TreeNode(1), TreeNode(1)))

    def test_left_leaf_right_leaf(self):
        self.assertFalse(isSameTree(
            binarytree([1, 2]),
            binarytree([1, None, 2])
        ))

    def test_diffferent_leaves(self):
        self.assertFalse(isSameTree(
            binarytree([1, 2, 1]),
            binarytree([1, 1, 2])
        ))

    def test_larger_case(self):
        self.assertTrue(isSameTree(
            binarytree([1, 2, 6, 3, 4, None, None, None, None, 5]),
            binarytree([1, 2, 6, 3, 4, None, None, None, None, 5])
        ))

if __name__ == "__main__":
    main()