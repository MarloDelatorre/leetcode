from collections import deque
from typing import List
from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def averageOfLevels(root: TreeNode) -> List[float]:
    if not root:
        return []
    averages = []
    queue = deque([root]) 
    while queue:
        level_size = len(queue)
        sum = 0
        for _ in range(level_size):
            node = queue.popleft()
            sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        averages.append(sum / level_size)
    return averages

class Test(TestCase):
    def test_given_case(self):
        self.assertListEqual(
            averageOfLevels(binarytree([3, 9, 20, None, None, 15, 7])),
            [3, 14.5, 11]
        )

    def test_empty_tree(self):
        self.assertEqual(averageOfLevels(None), [])

    def test_single_value(self):
        self.assertEqual(averageOfLevels(binarytree([2])), [2])

if __name__ == "__main__":
    main()