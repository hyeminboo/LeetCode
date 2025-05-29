class Solution:
    def uniquePathsWithObstacles(self, obs: List[List[int]]) -> int:
        m, n = len(obs), len(obs[0])
        dp = [[0] * n for _ in range(m)]

        if obs[0][0] == 1:
            return 0

        def checkObs(i, j):
            return obs[i][j] != 1
        
        for i in range(m):
            for j in range(n):
                if checkObs(i, j):
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        print(dp)
        return dp[-1][-1]
            