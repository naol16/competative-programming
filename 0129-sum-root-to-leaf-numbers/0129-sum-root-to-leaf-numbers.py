# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        newlist=[]
        totalsum=0
        def preorder(node,currentpath):
              nonlocal totalsum,newlist
              
             
              currentpath+=str(node.val)
              if not node.left and not node.right:
                 newlist.append(currentpath)
                 return
              if node.left:
                 preorder(node.left,currentpath)
              if node.right:
                 preorder(node.right,currentpath)
        preorder(root,'')
        for i in newlist:
            length=len(i)-1
            total1=0
            for j in i:
                total1+=int(j)*pow(10,length)
                length-=1
                
            totalsum+=total1
          
        return totalsum
            
            
        
            
        