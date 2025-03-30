class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        x = []
        for i in range(n):
            x.append(points[i][0])
        
        ans = []
        for i in range(n-1):
            ans.append(abs(x[i + 1] - x[i]))
        
        return max(ans)