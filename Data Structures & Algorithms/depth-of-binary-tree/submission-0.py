# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        
        def postOT(node: Optional[TreeNode], depth: int) -> None:
            nonlocal max_depth
            if node is None:
                return
            max_depth = max(max_depth, depth)
            postOT(node.left, depth + 1)
            
            postOT(node.right, depth + 1)
            
        postOT(root,1)
        return max_depth