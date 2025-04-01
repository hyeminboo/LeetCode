class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sols = [[sum(s), i] for i, s in enumerate(mat)]
        sols.sort()

        return [sol[1] for sol in sols[:k]]
