class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        div = n // 3
        piles.sort(reverse=True)
        pile = piles[:-div:]

        ans = 0
        for i in range(len(pile)):
            if i % 2 != 0:
                ans += pile[i]

        return ans

