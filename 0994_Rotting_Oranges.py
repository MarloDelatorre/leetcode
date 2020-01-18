from collections import deque
from typing import List
from unittest import TestCase, main

def orangesRotting(grid: List[List[int]]) -> int:
    minutes = 0
    queue = deque()
    fresh_orange_count = 0

    for r, row in enumerate(grid):
        for c, element in enumerate(row):
            if element == 1:
                fresh_orange_count += 1
            elif element == 2:
                queue.append((r, c))

    while fresh_orange_count > 0:
        prev_fresh_orange_count = fresh_orange_count
        size = len(queue)
        for _ in range(size):
            r, c = queue.popleft()
            if c - 1 >= 0 and grid[r][c - 1] == 1:
                grid[r][c - 1] = 2
                queue.append((r, c - 1)) 
                fresh_orange_count -= 1
            if c + 1 < len(grid[r]) and grid[r][c + 1] == 1:
                grid[r][c + 1] = 2
                queue.append((r, c + 1))
                fresh_orange_count -= 1
            if r - 1 >= 0 and grid[r - 1][c] == 1:
                grid[r - 1][c] = 2
                queue.append((r - 1, c))
                fresh_orange_count -= 1
            if r + 1 < len(grid) and grid[r + 1][c] == 1:
                grid[r + 1][c] = 2
                queue.append((r + 1, c))
                fresh_orange_count -= 1
        if prev_fresh_orange_count == fresh_orange_count:
            return -1
        minutes += 1

    return minutes

class Test(TestCase):
    def test_given_case_1(self):
        self.assertEqual(orangesRotting([
            [2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]
        ]), 4)

    def test_given_case_2(self):
        self.assertEqual(orangesRotting([
            [2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]
        ]), -1) 

    def test_given_case_3(self):
        self.assertEqual(orangesRotting([[0, 2]]), 0)

    def test_only_fresh(self):
        self.assertEqual(orangesRotting([[1]]), -1)
    
    def test_no_oranges(self):
        self.assertEqual(orangesRotting([[0]]), 0)

    def test_one_fresh_one_rotten(self):
        self.assertEqual(orangesRotting([[1, 2]]), 1)

if __name__ == "__main__":
    main()