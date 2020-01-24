from typing import List
from unittest import TestCase, main

def isValidSudoku(board: List[List[str]]) -> bool:
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    subbox_sets = [[set() for _ in range(3)] for _ in range(3)]
    
    for row in range(9):
        for col in range(9):
            cell = board[row][col]
            if cell != '.':
                subbox_row = row // 3
                subbox_col = col // 3
                if cell in col_sets[col] or \
                    cell in row_sets[row] or \
                    cell in subbox_sets[subbox_row][subbox_col]:
                        return False
                col_sets[col].add(cell)
                row_sets[row].add(cell)
                subbox_sets[subbox_row][subbox_col].add(cell)
    return True

class Test(TestCase):
    def test_given_true_case(self):
        self.assertTrue(isValidSudoku([
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]))

    def test_given_false_case(self):
        self.assertFalse(isValidSudoku([
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]))

if __name__ == "__main__":
    main()