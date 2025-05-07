class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ans = [x for x in edges[0] if x in edges[1]]
        return ans[0]