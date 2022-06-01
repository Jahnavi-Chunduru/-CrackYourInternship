def shortestBridge(self, A: List[List[int]]) -> int:
        row,col = len(A),len(A[0])
        dirs = [(0,0),(-1,0),(0,-1),(1,0),(0,1)]
        island1 = collections.deque()
        def dfs(x,y):
            for dx, dy in dirs:
                if 0<=x+dx<row and 0<=y+dy<col and A[x+dx][y+dy]==1:
                    A[x+dx][y+dy]=2
                    island1.append([x+dx,y+dy])
                    dfs(x+dx,y+dy)
        def findIsland1():
            for x in range(row):
                for y in range(col):
                    if A[x][y]:
                        return dfs(x,y)
        findIsland1()
        step = 0
        while island1:
            for _ in range(len(island1)):
                x,y=island1.popleft()
                for dx,dy in dirs:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<row and 0<=ny<col and A[nx][ny]!=2:
                        if A[nx][ny] == 0:
                            A[nx][ny]=2
                            island1.append([nx,ny])
                        elif A[nx][ny] == 1:
                            return step
            step+=1
        return step
