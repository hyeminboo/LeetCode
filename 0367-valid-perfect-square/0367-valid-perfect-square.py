class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        n = num // 2
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == num:
                return True
            
            if mid ** 2 > num :
                right = mid - 1
            else:
                left = mid + 1

        return False

