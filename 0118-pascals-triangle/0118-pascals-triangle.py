class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for n in range(1, numRows+1):
            tmp = [1] * n
            if len(ans) > 1:
                for i in range(1, n-1):
                    tmp[i] = ans[-1][i] + ans[-1][i-1]
            ans.append(tmp)
        
        return ans
