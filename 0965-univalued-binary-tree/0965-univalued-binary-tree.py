# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import  deque 
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val=root.val
        queue=deque([root])
        while queue:
              r=queue.popleft()
              if r.val!=val:
                 return False
              if r.left:
                 queue.append(r.left)
              if r.right:
                 queue.append(r.right)

        return True
        
              
                 
        
        