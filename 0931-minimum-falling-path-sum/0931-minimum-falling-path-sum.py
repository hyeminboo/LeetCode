class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        dp[0] = matrix[0]

        for i in range(n):
            for j in range(n):
                curr = matrix[i][j]
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + curr
                elif j == (n - 1):
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + curr
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1], dp[i-1][j-1]) + curr
        
        return min(dp[-1])