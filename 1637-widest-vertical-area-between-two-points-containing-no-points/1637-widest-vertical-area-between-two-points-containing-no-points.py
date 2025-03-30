class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        n = len(points)
        tmp = []
        for i in range(n):
            tmp.append(points[i][1])
        
        tmp.sort()
        return tmp[-1] - tmp[-2] - 1