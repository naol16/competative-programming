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
        qeue = deque([root])
        
        while qeue:
            length = len(qeue)
            temp = []
            for i in range(length):
                value = qeue.pop()
                temp.append(value.val)
                if value.left:
                    qeue.appendleft(value.left)
                if value.right:
                    qeue.appendleft(value.right)
            answer.append(temp)
        return answer

                 
