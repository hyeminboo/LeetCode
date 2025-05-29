class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[float('inf')] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(len(triangle[i])):
                curr = triangle[i][j]
                if j == 0:
                    dp[i][j] = dp[i-1][j] + curr
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + curr
        
        return min(dp[-1])
