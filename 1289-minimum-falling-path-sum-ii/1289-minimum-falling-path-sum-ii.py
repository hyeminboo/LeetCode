class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        dp[0] = grid[0]

        def findmin(i, j):
            minval = float('inf')
            for k in range(n):
                if j == k:
                    continue
                else:
                    minval = min(minval, dp[i-1][k])
            return minval

        for i in range(1, n):
            for j in range(n):
                curr = grid[i][j]
                dp[i][j] = findmin(i, j) + curr
        
        return min(dp[-1])
