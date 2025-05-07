class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n

        def dfs(city):
            for c in range(n):
                if isConnected[city][c] == 1 and visited[c] == 0:
                    visited[c] = 1
                    dfs(c)
        
        prov = 0
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                dfs(i)
                prov += 1

        return prov