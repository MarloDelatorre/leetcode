from typing import List
from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree, to_list

def preorderTraversal(root: TreeNode) -> List[int]:
    nodes = []
    traverse(root, nodes)
    return nodes 

def traverse(root: TreeNode, nodes: List[int]):
    if root is None:
        return
    nodes.append(root.value)
    traverse(root.left, nodes)
    traverse(root.right, nodes)

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            preorderTraversal(binarytree([1, None, 2, 3])),
            [1, 2, 3]
        )

    def test_empty_tree(self):
        self.assertEqual(preorderTraversal(None), [])

    def test_middle_nodes(self):
        self.assertListEqual(
            preorderTraversal(binarytree([1, 2, 3, None, 4, 5])),
            [1, 2, 4, 3, 5]
        )

if __name__ == "__main__":
    main()