from typing import List
from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree, to_list

def inorderTraversal(root: TreeNode) -> List[int]:
    nodes = []
    traverse(root, nodes)
    return nodes 

def traverse(root: TreeNode, nodes: List[int]):
    if root is None:
        return
    traverse(root.left, nodes)
    nodes.append(root.val)
    traverse(root.right, nodes)

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            inorderTraversal(binarytree([1, None, 2, 3])),
            [1, 3, 2]
        )

    def test_empty_tree(self):
        self.assertEqual(inorderTraversal(None), [])

    def test_middle_nodes(self):
        self.assertListEqual(
            inorderTraversal(binarytree([1, 2, 3, None, 4, 5])),
            [2, 4, 1, 5, 3]
        )

if __name__ == "__main__":
    main()