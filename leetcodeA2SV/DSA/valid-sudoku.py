class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            v = set()
            for j in range(9):
                if board[i][j] not in v:
                    if board[i][j].isdigit():
                        #print(board[i][j], board[i][j].isdigit())
                        v.add(board[i][j])
                        
                else:
                    return False


        for i in range(9):
            v = set()
            for j in range(9):
                if board[j][i] not in v:
                    if board[j][i].isdigit():
                        v.add(board[j][i])
                        
                else:
                    return False


        p = [(0,0), (0,3), (0,6), (3,0), (3, 3), (3,6), (6,0), (6,3),(6,6)]

        for el in p:
            row, col = el
            v = set()
            for r in range(row, row+3):
                for c in range(col, col+3):
                    if board[r][c] not in v:
                       if board[r][c].isdigit():
                            v.add(board[r][c])
                    else:
                        return False

            





           

        return True



        
