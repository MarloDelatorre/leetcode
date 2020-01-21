from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def isSymmetric(root: TreeNode) -> bool:
    def are_symmetric(s: TreeNode, t: TreeNode):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and are_symmetric(s.left, t.right) and are_symmetric(s.right, t.left)
        
    return not root or are_symmetric(root.left, root.right) 

class Test(TestCase):
    def test_given_case_1(self):
        self.assertTrue(isSymmetric(binarytree([1, 2, 2, 3, 4, 4, 3])))

    def test_given_case_2(self):
        self.assertFalse(isSymmetric(binarytree([1, 2, 2, None, 3, None, 3]))) 

    def test_empty_tree(self):
        self.assertTrue(isSymmetric(None))

    def test_single_node(self):
        self.assertTrue(isSymmetric(TreeNode(1)))
    
    def test_null_child(self):
        self.assertFalse(isSymmetric(binarytree([1, 2, 2, 2, None, 2])))

    def test_one_child(self):
        self.assertFalse(isSymmetric(binarytree([1, 0])))

    def test_diamond(self):
        self.assertTrue(isSymmetric(binarytree([1, 2, 2, None, 3, 3])))

if __name__ == "__main__":
    main()