class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        acc = [nums[0]]

        for i in range(1, len(nums)):
            acc.append(acc[-1] + nums[i])
        
        def find_num(query):
            left, right = 0, len(acc)-1
            while left <= right:
                mid = (left + right) // 2
                if acc[mid] == query:
                    return mid + 1

                if acc[mid] > query:
                    right = mid - 1
                else:
                    left = mid + 1
        
            return left

        return [find_num(q) for q in queries]

