class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        indegree = [0] * numCourses
        ans = []

        for a, b in prerequisites:
            pre[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            ans.append(curr)
            for i in pre[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        
        return ans