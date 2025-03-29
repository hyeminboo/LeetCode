class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        각 층 k 에서 필요한 코인 수 : k * (k + 1) / 2
        n의 mid에서 구한 코인 수 < n이라면 left 증가, 아니라면 right 감소
        """

        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            num = mid * (mid + 1) // 2

            if n == num:
                return mid
            
            if n > num:
                left = mid + 1
            else:
                right = mid - 1
        
        return right