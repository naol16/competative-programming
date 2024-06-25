# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        if not root:
            return []
        answer = []
        que = deque([root])
        
        while que:
            length = len(que)
            temp = []
            for i in range(length):
                node = que.pop()
                temp.append(node.val)
                if node.left:
                    que.appendleft(node.left)
                if node.right:
                    que.appendleft(node.right)
            answer.append(temp)
        return answer

                 
