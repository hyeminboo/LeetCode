class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] == target:
                return [i, i+1]
            elif nums[i] + nums[i+1] >= target:
                continue
