class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        area = 0
        visited = set()
        def dfs(r,c):

            if ((r,c) in visited or grid[r][c]==0):
                return 0
            visited.add((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            cur_area = 1
            for dr,dc in directions:
                nr = dr+r
                nc = dc+c
                if (nr in range(row) and nc in range(col) and grid[nr][nc] == 1 and (nr,nc) not in visited):
                    
                    cur_area += dfs(nr,nc)
                
            return cur_area
        
        for i in range (row):
            for j in range (col):
                if grid[i][j] == 1 and (i,j) not in visited:
                    curr_area = dfs(i,j)

                    area = max(area,curr_area)
        return (area)
            
            
