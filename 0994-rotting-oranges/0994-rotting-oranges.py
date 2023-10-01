class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        start_rot = []
        visited = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                visited[(i, j)] = False
                if grid[i][j] == 2:
                    start_rot.append((i, j, 0))
                    
        queue = []
        queue += start_rot
        
        cnt = 0
        while queue:
            x, y, c = queue.pop(0)
            
            if visited[(x, y)] == False:
                visited[(x, y)] = True
                cnt = c
                
                if x + 1 < len(grid) and grid[x + 1][y] == 1:
                    queue.append((x + 1, y, c + 1))
                if x - 1 >= 0 and grid[x - 1][y] == 1:
                    queue.append((x - 1, y, c + 1))    
                if y + 1 < len(grid[0]) and grid[x][y + 1] == 1:
                    queue.append((x, y + 1, c + 1))
                if y - 1 >= 0 and grid[x][y - 1] == 1:
                    queue.append((x, y - 1, c + 1))
                    
                grid[x][y] = 2

        # Check if there are any fresh oranges left
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        return cnt

