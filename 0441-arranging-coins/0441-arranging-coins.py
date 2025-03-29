class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
            
        n_copy = n + 1
        ans = 0

        for i in range(1, n_copy):
            n -= i
            if n <= 0:
                return ans        
            ans += 1