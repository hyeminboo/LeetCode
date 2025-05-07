class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        ans = []
        indegree = [0] * numCourses

        for a, b in prerequisites:
            pre[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            ans.append(i)
            for i in pre[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

        return len(ans)  == numCourses