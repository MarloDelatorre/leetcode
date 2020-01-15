from typing import List
from unittest import main, TestCase

from datastructures.tree import TreeNode

def preorder(root: TreeNode) -> List[int]:
    nodes = []
    traverse(root, nodes)
    return nodes

def traverse(root: TreeNode, nodes: List[int]):
    if root is None:
        return

    nodes.append(root.val)
    for node in root.children:
        traverse(node, nodes)

class Test(TestCase):
    def test_given_case(self):
        raise NotImplementedError("Need tree utils to implement tests")

if __name__ == "__main__":
    main()