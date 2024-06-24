# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        numbersum=0
    
        def dfs(root,parent,grandparent):
            nonlocal numbersum
            
            if grandparent:
               if grandparent.val%2==0:
                  numbersum+=root.val
               if not root:
                  return
               
            
            if not root.left and not root.right:
               return
            if root.left:
               dfs(root.left,root,parent)
            if root.right:
               dfs(root.right,root,parent)
    
          
        dfs(root,None,None)
        
        return numbersum
            
        