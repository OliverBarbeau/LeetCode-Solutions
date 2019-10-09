class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for item in row:
                if item != ".":
                    if item not in s and int(item) <= 9 and int(item) >= 1:
                        
                        s.add(item)
                        
                    else:
                        return False
        for column in range(9):
            s = set()
            for row in board:
                if row[column] != ".":
                    if row[column] not in s:
                        s.add(row[column])
                    else:
                        return False
        for boxI in range(3):
            for boxJ in range(3):
                s = set()
                for i in range(boxI*3, boxI*3+3):
                    for j in range(boxJ*3,boxJ*3+3):
                        if board[i][j] != ".":
                            if board[i][j] not in s:
                                s.add(board[i][j])
                            else:
                                return False
        return True