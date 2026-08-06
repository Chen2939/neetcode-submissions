class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0
        
        def bfs(row, col):
            q = deque()
            dv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited.add((row, col))
            q.append((row, col))
            
            while q:
                r, c = q.popleft()
                for dr, dc in dv:
                    row, col = r + dr, c + dc
                    if (row in range(ROWS) and col in range(COLS) 
                        and grid[row][col] == "1" and (row, col) not in visited):
                        q.append((row, col))
                        visited.add((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    res += 1
                
        return res