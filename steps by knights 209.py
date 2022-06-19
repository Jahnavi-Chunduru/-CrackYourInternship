from collections import deque
class Solution:
    def isValid(self, x, y, N):
        return (x >= 0 and x < N and y >= 0 and y < N)
    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        dxy = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
        KnightPos[0]-=1
        KnightPos[1]-=1
        TargetPos[0]-=1
        TargetPos[1]-=1
        vis = [[False for i in range(N)] for j in range(N)]
        q = deque()
        q.append([KnightPos[0], KnightPos[1], 0])
        vis[KnightPos[0]][KnightPos[1]] = True
        
        while(len(q)):
            cur = q.popleft()
            x = cur[0]
            y = cur[1]
            steps = cur[2]
            if(x == TargetPos[0] and y == TargetPos[1]):
                return steps
            for i in range(8):
                
                n_x = x + dxy[i][0]
                n_y = y + dxy[i][1]
                if(self.isValid(n_x, n_y, N) and vis[n_x][n_y] == False):
                    q.append([n_x, n_y, steps + 1])
                    vis[n_x][n_y] = True
        return -1
        
        
        
