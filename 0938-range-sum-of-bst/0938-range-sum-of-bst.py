# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def sumBST(node):
            if not node:
                return 0
            
            curr = 0
            if low <= node.val <= high:
                curr = node.val

            left_sum = sumBST(node.left)
            right_sum = sumBST(node.right)

            return curr + left_sum + right_sum
        
        return sumBST(root)