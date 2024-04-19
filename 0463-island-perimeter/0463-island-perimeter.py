class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        visited = set()

        def check(i, j):
            nonlocal peri
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                peri += 1

        def dfs(i, j):
            if (i, j) in visited:
                return
            visited.add((i, j))
            check(i - 1, j)
            check(i + 1, j)
            check(i, j - 1)
            check(i, j + 1)
            if i > 0 and grid[i - 1][j] == 1:
                dfs(i - 1, j)
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                dfs(i + 1, j)
            if j > 0 and grid[i][j - 1] == 1:
                dfs(i, j - 1)
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                dfs(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)

        return peri
