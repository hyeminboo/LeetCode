class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                if i == 0:
                    dp[i+1][j+1] += dp[i+1][j] + curr
                elif j == 0:
                    dp[i+1][j+1] += dp[i][j+1] + curr
                else:
                    dp[i+1][j+1] += min(dp[i+1][j], dp[i][j+1]) + curr
        
        return dp[-1][-1]

