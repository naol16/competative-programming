# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth=0
        def  finding_depth(root,current):
             nonlocal max_depth
             max_depth=max(max_depth,current)
             if not root:
                return 
             finding_depth(root.left,current+1)
             finding_depth(root.right,current+1)
        finding_depth(root,0)
        return max_depth
             
        