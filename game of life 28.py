class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        for r in range(len(board)):
            for c in range(len(board[0])):
                countLives = 0
                
                for newRow, newCol in [(r-1,c-1), (r-1,c), (r-1,c+1), (r,c-1), (r,c+1), (r+1,c-1), (r+1,c), (r+1,c+1)]:
                    if newRow < 0 or newRow == len(board) or newCol < 0 or newCol == len(board[0]):
                        continue
                    if abs(board[newRow][newCol]) == 1:
                        countLives += 1
                
                if board[r][c] == 1 and (countLives < 2 or countLives > 3):
                    board[r][c] = -1
                elif board[r][c] == 0 and countLives == 3:
                    board[r][c] = 2
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == -1:
                    board[r][c] = 0
