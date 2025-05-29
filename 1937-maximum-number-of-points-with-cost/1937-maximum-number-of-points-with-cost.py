class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prev = points[0]

        for i in range(1, m):
            left = [0] * n
            right = [0] * n
            curr = [0] * n

            left[0] = prev[0]
            for j in range(1, n):
                left[j] = max(left[j-1]-1, prev[j])
            
            right[n-1] = prev[n-1]
            for j in range(n-2, -1, -1):
                right[j] = max(right[j+1]-1, prev[j])
            
            for j in range(n):
                curr[j] = max(left[j], right[j]) + points[i][j]
            
            prev = curr
        
        return max(prev)