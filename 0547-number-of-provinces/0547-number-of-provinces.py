class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n

        def dfs(city):
            for i in range(n):
                if isConnected[city][i] == 1 and not visited[i]:
                    visited[i] = 1
                    dfs(i)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                dfs(i)
                provinces += 1

        return provinces