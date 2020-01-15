from typing import List
from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree, to_list

def postorderTraversal(root: TreeNode) -> List[int]:
    nodes = []
    traverse(root, nodes)
    return nodes 

def traverse(root: TreeNode, nodes: List[int]):
    if root is None:
        return
    traverse(root.left, nodes)
    traverse(root.right, nodes)
    nodes.append(root.val)

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            postorderTraversal(binarytree([1, None, 2, 3])),
            [3, 2, 1]
        )

    def test_empty_tree(self):
        self.assertEqual(postorderTraversal(None), [])

    def test_middle_nodes(self):
        self.assertListEqual(
            postorderTraversal(binarytree([1, 2, 3, None, 4, 5])),
            [4, 2, 5, 3, 1]
        )

if __name__ == "__main__":
    main()