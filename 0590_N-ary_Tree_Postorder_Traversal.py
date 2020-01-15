from typing import List
from unittest import main, TestCase

from datastructures.tree import TreeNode

def postorder(root: TreeNode) -> List[int]:
    nodes = []
    traverse(root, nodes)
    return nodes

def traverse(root: TreeNode, nodes: List[int]):
    if root is None:
        return

    for node in root.children:
        traverse(node, nodes)
    nodes.append(root.val)

class Test(TestCase):
    def test_given_case(self):
        raise NotImplementedError("Need tree utils to implement tests")

if __name__ == "__main__":
    main()