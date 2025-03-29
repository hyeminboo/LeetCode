class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]

        index = 0
        if target in letters:
            index = letters.index(target)
        left, right = index, len(letters) - 1

        while left < right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid - 1
                flag = 0
            else:
                left = mid + 1
                flag = 1
        
        if letters[left] > target:
            return letters[left]

        if flag == 0:
            return letters[right + 1]
        else:
            return letters[left - 1]
            
