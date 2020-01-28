from collections import deque
from typing import List, Deque
from unittest import TestCase, main

def numIslands(grid: List[List[str]]) -> int:
    count = 0
    queue = deque()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                count += 1
                explore(grid, row, col, queue)

    return count

def explore(grid: List[List[str]], row: int, col: int, queue: Deque):
    queue.append((row, col))
    while queue:
        r, c = queue.popleft()
        grid[r][c] = 0
        if r - 1 >= 0 and grid[r - 1][c] == 1:
            queue.append((r - 1, c))
        if r + 1 < len(grid) and grid[r + 1][c] == 1:
            queue.append((r + 1, c))
        if c - 1 >= 0 and grid[r][c - 1] == 1:
            queue.append((r, c - 1))
        if c + 1 < len(grid[0]) and grid[r][c + 1] == 1:
            queue.append((r, c + 1))

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(
            numIslands([
                [1, 1, 1, 1, 0],
                [1, 1, 0, 1, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]),
            1
        )

    def test_given_case_2(self):
        self.assertEqual(
            numIslands([
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1]
            ]),
            3
        )

if __name__ == "__main__":
    main() 