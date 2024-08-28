class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        count = 0
        def dfs(r,c,visited):   
            
            if r < 0 or r >= len(grid2) or c < 0 or c >= len(grid2[0]) or visited[r][c] or grid2[r][c] == 0:
                return True
            
            if grid1[r][c] == 0:
                return False
            visited[r][c] = True
            u = dfs(r+1,c,visited)
            d = dfs(r,c+1,visited)
            l = dfs(r-1,c,visited)
            r = dfs(r,c-1,visited)

            return u and d and l and r
            

        visited = [[False for c in range(cols)]for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1 and not visited[r][c]:
                    if dfs(r,c,visited):
                        count += 1
        return count



