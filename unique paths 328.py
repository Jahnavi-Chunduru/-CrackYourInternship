class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        
        count = 0
        n = len(grid)
        m = len(grid[0])
        
        def dfs(row,col,move):
            
        
            nonlocal count
            
            if row < 0 or row >= n or col < 0 or col >= m or grid[row][col] == -1 or \
            grid[row][col] == 3:
                return
            
            if grid[row][col] == 2:
                if move == non_obstacle:
                    count +=1
                return
            
            move += 1
            grid[row][col] = 3
            
            dfs(row+1,col,move)
            dfs(row-1,col,move)
            dfs(row,col+1,move)
            dfs(row,col-1,move)
            
            grid[row][col] = 0
            
        
        non_obstacle = 0
    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row,col = i,j
                    
                if grid[i][j] != -1:
                    non_obstacle += 1
                    
                    
        dfs(row,col,1)
        return count
