from typing import List
from unittest import TestCase, main

def islandPerimeter(grid: List[List[int]]) -> int:
    borders = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                top_is_land = row - 1 >= 0 and grid[row - 1][col] == 1
                left_is_land = col - 1 >= 0 and grid[row][col - 1] == 1
                if top_is_land and left_is_land:
                    continue
                elif top_is_land or left_is_land:
                    borders += 2
                elif not top_is_land and not left_is_land:
                    borders += 4
    return borders

class Test(TestCase):
    def test_given_case(self):
        self.assertEqual(
            islandPerimeter([
                [0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [1, 1, 0, 0]
            ]),
            16
        )

    def test_single_island(self):
        self.assertEqual(
            islandPerimeter([
                [0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]),
            4
        ) 
    
    def test_vertical_strip(self):
        self.assertEqual(
            islandPerimeter([
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0]
            ]),
            10
        )  

    def test_horizontal_strip(self):
        self.assertEqual(
            islandPerimeter([
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]),
            10
        )   
    
    def test_square_island(self):
        self.assertEqual(
            islandPerimeter([
                [0, 0, 0, 0],
                [0, 1, 1, 1],
                [0, 1, 1, 1],
                [0, 1, 1, 1]
            ]),
            12 
        )

if __name__ == "__main__":
    main()