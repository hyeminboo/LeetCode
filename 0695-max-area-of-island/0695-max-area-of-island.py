class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = [0]
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            num = 1
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                dirs = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
                        num += 1
            
            return num
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    islands.append(bfs(r, c))

        return max(islands)