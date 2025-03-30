class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_r = sorted(nums)[::-1]
        n = len(nums)
        tmp = 0
        ans = {}

        for i in range(n):
            curr = nums_r[i]
            if tmp != curr:
                tmp = curr
                ans[curr] = n - i - 1
            else:
                ans[curr] -= 1
        
        ans_list = []
        for i in nums:
            ans_list.append(ans[i])
        
        return ans_list

