# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        visited = {}
        def dfs(node):
            if node not in visited:
                visited[node] = node.next
            else:
                return True

            if node.next is None:
                return False

            return dfs(node.next)
        
        return dfs(head)