class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def sorting(arr):
            if len(arr) <= 1:
                return arr

            m = (len(arr) - 1) // 2

            low = [x for x in arr if x < arr[m]]
            mid = [x for x in arr if x == arr[m]]
            high = [x for x in arr if x > arr[m]]

            if len(low) == 0:
                return mid + sorting(high)
            elif len(high) == 0:
                return sorting(low) + mid
            
            return sorting(low) + mid + sorting(high)
        
        new_nums = sorting(nums)
        new_nums = new_nums[::-1]
        return new_nums[k-1]