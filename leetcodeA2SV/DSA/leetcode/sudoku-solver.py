from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        three_by_threes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    cols[c].add(val)
                    rows[r].add(val)
                    three_by_threes[(r//3,c//3)].add(val)

        
        def backtrack(r, c):
            if r == 9:
                return True 
            
            if c == 9:
                return backtrack(r + 1, 0)  
            
            if board[r][c] == ".":
                for val in map(str, range(1, 10)):
                    if (val not in cols[c] and
                        val not in rows[r] and
                        val not in three_by_threes[(r//3, c//3)]):
                        
                        board[r][c] = val
                        cols[c].add(val)
                        rows[r].add(val)
                        three_by_threes[(r//3, c//3)].add(val)
                        
                        if backtrack(r, c + 1):
                            return True
                       
                        board[r][c] = "."
                        cols[c].remove(val)
                        rows[r].remove(val)
                        three_by_threes[(r//3, c//3)].remove(val)
                        
            else:
                return backtrack(r, c + 1)  
            
            return False  
        backtrack(0, 0)
