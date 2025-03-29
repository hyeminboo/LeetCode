class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        min_index = 0

        for i in range(n):
            for j in range(min_index, n):
                if fruits[i] <= baskets[j]:
                    fruits[i] = baskets[j] = 0
                    min_index = min(min_index, j)
                    break
                   
       
        return len([x for x in baskets if x != 0])