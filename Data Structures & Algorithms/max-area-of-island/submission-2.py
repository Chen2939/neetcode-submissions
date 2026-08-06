class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (r<0 or c<0 or c==COLS or r==ROWS or grid[r][c]!=1 or (r, c) in visited):
                return 0
            visited.add((r, c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))

        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        return res