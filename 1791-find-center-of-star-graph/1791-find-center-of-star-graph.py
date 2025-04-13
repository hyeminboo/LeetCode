class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        check = []
        for e in edges:
            if len(check) > 0:
                check = [x for x in check if x in e]
            else:
                check.append(e[0])
                check.append(e[1])
        
        return check[0]