class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashmap = {}
        ans = []
        for i in nums:
            if i in hashmap.keys():
                ans.append(i)
            else:
                hashmap[i] = 1
        
        return ans
        