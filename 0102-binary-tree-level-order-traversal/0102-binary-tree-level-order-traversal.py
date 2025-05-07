from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        q = deque()
        q.append([root, 1])
        ans = defaultdict(list)
        ans[1].append(root.val)

        while q:
            node, depth = q.popleft()

            if node.left:
                q.append([node.left, depth+1])
                ans[depth+1].append(node.left.val)
            if node.right:
                q.append([node.right, depth+1])
                ans[depth+1].append(node.right.val)
        
        return list(ans.values())