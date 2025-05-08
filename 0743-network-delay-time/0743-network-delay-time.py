class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)

        for u,v,w in times:
            adj_list[u].append((w, v))
        
        visited = set()
        heap = [(0, k)]
        while heap:
            travel_time, node = heapq.heappop(heap)
            visited.add(node)

            if len(visited) == n:
                return travel_time
            
            for time, adj_node in adj_list[node]:
                if adj_node not in visited:
                    heapq.heappush(heap, (travel_time+time, adj_node))

        return -1