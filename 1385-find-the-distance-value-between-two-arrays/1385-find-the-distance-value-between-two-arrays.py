class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n = len(arr2)
        ans = 0
        for i in arr1:
            left = i - d
            right = i + d
            if len([x for x in arr2 if x < left or x > right]) == n:
                ans += 1
            
        return ans
