from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def isSubtree(s: TreeNode, t: TreeNode) -> bool:
    if not t:
        return True
    if not s:
        return False

    if s.val == t.val and is_equal(s, t):
        return True

    return isSubtree(s.left, t) or isSubtree(s.right, t)

def is_equal(s: TreeNode, t: TreeNode) -> bool:
    if not s and not t:
        return True
    if not s or not t:
        return False
    
    return s.val == t.val and is_equal(s.left, t.left) and is_equal(s.right, t.right)

class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(isSubtree(
            binarytree([3, 4, 5, 1, 2]),
            binarytree([4, 1, 2])
        ))

    def test_given_case_2(self):
        self.assertFalse(isSubtree(
            binarytree([3, 4, 5, 1, 2, None, None, None, None, 0]),
            binarytree([4, 1, 2])
        ))

    def test_empty_in_empty(self):
        self.assertTrue(isSubtree(None, None))

    def test_empty_in_single_node(self):
        self.assertTrue(isSubtree(TreeNode(1), None))

    def test_subtree_in_child(self):
        self.assertTrue(isSubtree(
            binarytree([1, 2, 3]),
            TreeNode(2)
        ))

    def test_not_found_in_tree(self):
        self.assertFalse(isSubtree(
            binarytree([1, 4, 5]),
            TreeNode(3)
        ))

if __name__ == "__main__":
    main()