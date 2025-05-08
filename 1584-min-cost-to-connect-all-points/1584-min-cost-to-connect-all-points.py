class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [0] * n
        pq = [(0, 0)]
        cache = {0: 0}
        min_cost = 0

        while pq:
            cost, u = heapq.heappop(pq)

            if visited[u]:
                continue
            
            visited[u] = 1
            min_cost += cost

            for v in range(n):
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                if dist < cache.get(v, float('inf')):
                    heapq.heappush(pq, (dist, v))

        return min_cost