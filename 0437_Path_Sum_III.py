from typing import List
from unittest import TestCase, main

from datastructures.binarytree import TreeNode, binarytree

def pathSum(root: TreeNode, k: int) -> int:
    count = 0

    def visit(node: TreeNode, sums: List[int]) -> None:
        nonlocal count, k
        if not node:
            return
        
        sums.append(0)
        for i in range(len(sums)):
            sums[i] += node.val 
            if sums[i] == k:
                count += 1

        visit(node.left, sums)
        visit(node.right, sums)

        sums.pop()
        for i in range(len(sums)):
            sums[i] -= node.val

    visit(root, [])
    return count

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(
            pathSum(binarytree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8),
            3
        )

    def test_empty_case(self):
        self.assertEqual(pathSum(None, 1), 0)

    def test_all_equal_k(self):
        self.assertEqual(pathSum(binarytree([1, 1, 1]), 1), 3)

if __name__ == "__main__":
    main()