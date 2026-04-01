class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        result = 0 
        visited = set()
        def dfs(r,c):
            if (r,c) in visited:
                return
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            visited.add((r,c))
            for (dr, dc) in directions:
                nr = dr+r
                nc = dc+c
                if (nr in range(row) and nc in range(col) and grid[nr][nc] == "1"):
                    dfs(nr,nc)
                    
        for i in range (row):
            for j in range (col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    result += 1
        return result
                