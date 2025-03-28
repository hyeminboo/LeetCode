class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(0, n-1):
            for j in range(i + 1, n):
                sum_num = nums[i]
                sum_num += nums[j]
                if sum_num < target:
                    ans += 1
                else:
                    continue
        
        return ans