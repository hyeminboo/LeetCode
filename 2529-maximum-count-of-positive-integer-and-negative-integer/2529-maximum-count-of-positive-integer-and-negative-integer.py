class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        if 0 in nums:
            i = nums.index(0)
            neg = i
            del nums[i]

            rNums = nums[::-1]
            if 0 in rNums:
                i = rNums.index(0)
                pos = i

            else: 
                pos = len(nums) - neg
            
            return max(pos, neg)
   
  
        
        left, right = 0, len(nums) - 1

        flag = 0
        while left < right:
            mid = (left + right) // 2

            if nums[mid] * nums[mid-1] < 0:
                return max(mid, len(nums)-mid)
            
            if nums[mid] * nums[mid+1] < 0:
                return max(mid+1, len(nums)-mid-1)

            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1

        return len(nums)            