# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

class Solution:
    board = []
    def adjList(self, i, j):
        if j > 0:
            left = (i,j-1)
        else:
            left = None
        if j < len(self.board[0])-1:
            right = (i,j+1)
        else:
            right = None
        if i > 0:
            up = (i-1,j)
        else:
            up = None
        if i < len(self.board)-1:
            down = (i+1,j)
        else:
            down = None
        return [left,right,up,down]
    def findNext(self, word, i, j, checked):
        checked.add((i,j))
        if word == "":
            return True
        res = False
        neighbors = self.adjList(i,j)
        for neigh in neighbors:
            if neigh is not None:
                i, j = neigh
                if (i,j) not in checked and self.board[i][j] == word[0]:
                    res = res or self.findNext( word[1:], i, j, checked.copy())
        return res
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        found = False
        for i in range(len(board)):
            j = 0
            while j < len(board[0]) and not found:
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    else:
                        found = self.findNext(word[1:], i,j, set())
                j+=1
        return found