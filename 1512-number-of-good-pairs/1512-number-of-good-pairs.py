class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num = {}
        for i in nums:
            if i in num.keys():
                num[i] += 1
            else:
                num[i] = 1
        
        ans = 0
        for i in num.values():
            if i != 1:
                ans += (i * (i - 1)) // 2
        
        return ans