from collections import deque
from typing import List
from unittest import main

from datastructures.binarytree import TreeNode, binarytree
from testutil import ListOfListsTestCase

def levelOrderBottom(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    levels_bottomup = deque()
    queue = deque([root])

    while queue:
        size = len(queue)
        level = []
        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels_bottomup.appendleft(level)

    return levels_bottomup

class Test(ListOfListsTestCase):
    def test_given_case(self):
        self.assert_list_of_lists_equal(
            levelOrderBottom(binarytree([3, 9, 20, None, None, 15, 7])),
            [[15, 7], [9, 20], [3]]
        )

    def test_empty_case(self):
        self.assertEqual(levelOrderBottom(None), [])

    def test_single_level(self):
        self.assert_list_of_lists_equal(
            levelOrderBottom(binarytree([1])),
            [[1]]
        )

if __name__ == "__main__":
    main()