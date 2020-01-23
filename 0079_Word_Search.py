from typing import List
from unittest import TestCase, main

def exist(board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        if not m or not n or not word:
            return False
        
        def search(row: int, col: int, index: int) -> bool:
            if index >= len(word):
                return True
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            if board[row][col] != word[index]:
                return False
            
            index += 1
            
            temp, board[row][col] = board[row][col], None
            
            found_next_letter = search(row - 1, col, index) or \
                    search(row + 1, col, index) or \
                    search(row, col - 1, index) or \
                    search(row, col + 1, index)
            
            board[row][col] = temp
            
            return found_next_letter
            
        for row in range(0, m):
            for col in range(0, n):
                if board[row][col] == word[0]:
                    if search(row, col, 0):
                        return True
                    
        return False

class Test(TestCase):
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]

    def test_given_case_1(self):
        self.assertTrue(exist(self.board, "ABCCED"))

    def test_given_case_2(self):
        self.assertTrue(exist(self.board, "SEE"))

    def test_given_case_3(self):
        self.assertFalse(exist(self.board, "ABCB"))

    def test_empty_word(self):
        self.assertFalse(exist(self.board, ""))

if __name__ == "__main__":
    main()