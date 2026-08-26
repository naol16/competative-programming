# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.

        """
        #the root is going to be compared 
        #the relationship is be
        #indicator
        #the grandroot
        #the root
        prev=None
        first=None
        second=None
        def dfs(root):
            nonlocal prev,first,second
            if not root :
               return 
            
            dfs(root.left)
            if prev and prev.val>root.val:
               if not first:
                  first=prev
               second=root
            prev=root
            dfs(root.right)
        dfs(root)
        first.val,second.val=second.val,first.val
        return root


        


                  
        

        
