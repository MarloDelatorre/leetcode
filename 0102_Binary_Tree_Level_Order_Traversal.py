from collections import deque
from typing import List
from unittest import main

from datastructures.binarytree import TreeNode, binarytree
from testutil import ListOfListsTestCase

def levelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    queue = deque()
    traversal = []

    queue.append(root)
    while queue:
        length = len(queue)
        level = []
        for _ in range(length):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        traversal.append(level)

    return traversal

class Test(ListOfListsTestCase):
    def test_given_case(self):
        self.assert_list_of_lists_equal(
            levelOrder(binarytree([3, 9, 20, None, None, 15, 7])),
            [[3], [9, 20], [15, 7]]
        )

    def test_empty_case(self):
        self.assertEqual(levelOrder(None), [])

    def test_single_level(self):
        self.assert_list_of_lists_equal(
            levelOrder(binarytree([1])),
            [[1]]
        )

if __name__ == "__main__":
    main()
