class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        ans = []

        for i in range(m):
            flag = 0
            tmp = nums[l[i]:r[i]+1:]
            tmp.sort()
            print(tmp)
            diff = tmp[0] - tmp[1]
            for j in range(1, len(tmp)-1):
                if diff != (tmp[j] - tmp[j+1]):
                    flag = 1
                    ans.append(False)
                    break
            if flag == 1:
                continue
            else:
                ans.append(True)
        
        return ans