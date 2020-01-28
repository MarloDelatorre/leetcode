from collections import deque
from typing import List
from unittest import main

from datastructures.binarytree import TreeNode, binarytree
from testutil import ListOfListsTestCase 

def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    left_to_right = True 
    queue = deque([root])
    levels = []

    while queue:
        size = len(queue)
        level = deque()
        for _ in range(size):
            node = queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)
        left_to_right = not left_to_right

    return [list(level) for level in levels]

class Test(ListOfListsTestCase):
    def test_given_case(self):
        self.assert_list_of_lists_equal(
            zigzagLevelOrder(binarytree([3, 9, 20, None, None, 15, 7])),
            [[3], [20, 9], [15, 7]]
        )

    def test_empty_tree(self):
        self.assert_list_of_lists_equal(zigzagLevelOrder(None), [])

    def test_root_node_only(self):
        self.assert_list_of_lists_equal(zigzagLevelOrder(TreeNode(1)), [[1]])

if __name__ == "__main__":
    main()