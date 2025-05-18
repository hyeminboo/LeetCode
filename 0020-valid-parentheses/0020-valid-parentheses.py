class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"(": ")", "{": "}", "[": "]"}
        pstack = deque()

        for i in s:
            if i == "(" or i == "[" or i == "{":
                pstack.append(i)
            else:
                if len(pstack) == 0:
                    return False

                p = pstack.pop()
                if pair[p] != i:
                    return False
        
        if len(pstack) > 0:
            return False
            
        return True