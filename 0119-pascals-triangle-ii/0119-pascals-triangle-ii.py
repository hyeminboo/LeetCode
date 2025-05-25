class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        ans = []
        for n in range(1, rowIndex+2):
            tmp = [1] * n
            if len(ans) > 1:
                for i in range(1, n-1):
                    tmp[i] = ans[-1][i] + ans[-1][i-1]
            ans.append(tmp)

        return ans[-1]