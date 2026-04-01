class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len((grid[0]))
        time = 0
        fresh = 0
        queue = collections.deque()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c]==1):
                    fresh+=1
                if (grid[r][c]==2):
                    queue.append((r,c))
        while queue and fresh>0:
            for i in range(len(queue)):
                curr, curc = queue.popleft()
                for dr,dc in directions:
                    row = curr +dr
                    col = curc + dc
                    if (row>=0 and col>=0 and row<rows and col<cols and grid[row][col]==1):
                        grid[row][col] = 2
                        queue.append((row,col))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
