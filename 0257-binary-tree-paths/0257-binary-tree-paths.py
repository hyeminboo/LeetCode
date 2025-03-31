# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def find_path(node, path, result):
            if not node:
                return
            else:
                path += str(node.val)
            
            if not node.left and not node.right:
                result.append(path)
                return
            
            else:
                find_path(node.left, path + '->', result)
                find_path(node.right, path + '->', result)
            
        result = []
        find_path(root, '', result)
        return result