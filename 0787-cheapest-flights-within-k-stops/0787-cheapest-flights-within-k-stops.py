class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf')] * n
        cost[src] = 0

        for _ in range(k+1):
            tmp = cost[:]
            for flight in flights:
                if cost[flight[0]] != float('inf'):
                    tmp[flight[1]] = min(tmp[flight[1]], cost[flight[0]]+flight[2])
            cost = tmp
        
        if cost[dst] != float('inf'):
            return cost[dst]
        else:
            return -1