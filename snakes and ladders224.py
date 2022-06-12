class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)
        lst_board = []
        rev = 1
        for row in board[::-1]:
            if rev == -1:
                lst_board+= row[::-1]
            else:
                lst_board+=row
            rev*=-1
        queue = deque([(1,0)])
        step_count = [float('inf') for _ in range(n*n)]
        step_count[0]=0 
        
        while queue:
            cur, step = queue.popleft()
            if cur==n*n:
                return step
            for i in range(1,7):
                nxt = cur+i
                if nxt>n*n:
                    nxt = n*n
                if lst_board[nxt-1]!=-1:
                    nxt = lst_board[nxt-1]
                if step_count[nxt-1]>step+1:
                    queue.append((nxt,step+1))
                    step_count[nxt-1] = step+1
     
        return -1
