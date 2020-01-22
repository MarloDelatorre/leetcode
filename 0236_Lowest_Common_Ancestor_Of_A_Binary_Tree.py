from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    lca = None

    def find_lca(node: TreeNode):
        nonlocal lca, p, q
        if not node:
            return (False, False)
        
        left_p, left_q = find_lca(node.left)
        right_p, right_q = find_lca(node.right)

        p_in_this_subtree = node.val == p.val or left_p or right_p 
        q_in_this_subtree = node.val == q.val or left_q or right_q

        if p_in_this_subtree and q_in_this_subtree:
            lca = node
            return (False, False)

        return (p_in_this_subtree, q_in_this_subtree)

    find_lca(root)
    return lca

class Test(TestCase):
    def test_given_case_1(self):
        raise Exception("Inserting precreated nodes in binary tree not yet supported")

if __name__ == "__main__":
    main()