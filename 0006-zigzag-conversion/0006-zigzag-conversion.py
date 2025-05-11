class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        if numRows == 2:
            r = 2
        elif numRows % 2 == 0:
            r = numRows + 2
        else:
            r = numRows + 1
        
        ans = [""] * numRows

        if r == 2:
            half = 0
        else:
            half = r // 2
            
        for i in range(len(s)):
            mod = i % r
   
            if mod <= half:
                ans[mod] += s[i]
            else:
                ans[r - mod] += s[i]

        answer = ""
        for i in ans:
            answer += i
        
        return answer