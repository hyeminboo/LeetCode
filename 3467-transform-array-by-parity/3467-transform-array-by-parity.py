class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if i % 2 == 0:
                ans.append(0)
            else:
                ans.append(1)
        
        ans.sort()

        return ans