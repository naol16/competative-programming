# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
           return[]
        answer=[]
        def dfs(root,val):
            if not root:
               return 
            if len(answer)==val:
               answer.append([])
            if val%2==0:
               answer[val].append(root.val)
            else:
                 answer[val].insert(0,root.val)
            dfs(root.left,val+1)
            dfs(root.right,val+1)
        dfs(root,0)
        return answer

            
