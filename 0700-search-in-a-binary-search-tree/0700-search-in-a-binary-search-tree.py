# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def finding(root,val):
            if not root:
               return 
            if root.val==val:
               return root
            if root.val>=val:
               return finding(root.left,val)
            if root.val<=val:
               return finding(root.right,val)
        if finding(root,val):
           return finding(root,val)
        else:
             return None
        