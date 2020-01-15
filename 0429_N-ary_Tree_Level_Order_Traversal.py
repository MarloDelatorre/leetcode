from collections import deque
from typing import List
from unittest import main, TestCase

from datastructures.tree import TreeNode

def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    nodes = []
    queue = deque([root])

    while queue:
        size = len(queue)
        level = []
        for _ in range(size):
            node = queue.popleft()
            if node.children:
                for child in node.children:
                    if child:
                        queue.append(child)
            level.append(node.val)
        nodes.append(level)

    return nodes

class Test(TestCase):
    def test_given_case(self):
        raise NotImplementedError("Need tree utils to implement tests")

if __name__ == "__main__":
    main()