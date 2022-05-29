class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    print("it is 1")
                    self.dfs(i, j,grid)
                    count +=1
        return count
        
    def dfs(self,row, col, grid):
        if row > len(grid)-1 or col > len(grid[0])-1 or col < 0 or row < 0:
            return
        elif grid[row][col] == '0':
            return
        else:
            grid[row][col] = '0' 
            print(row, col)
            self.dfs(row+1, col, grid)
            self.dfs(row-1, col, grid)
            self.dfs(row, col+1, grid)
            self.dfs(row, col-1, grid)
            
            
        
