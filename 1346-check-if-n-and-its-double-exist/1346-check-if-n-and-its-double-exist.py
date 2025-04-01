class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr = arr[::-1]
        if 0 in arr:
            arr.remove(0)

        for i in arr:
            if i % 2 == 0:
                if i // 2 in arr:
                    return True
        
        return False