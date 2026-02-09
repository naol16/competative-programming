1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
9        self.minabsolute=float('inf')
10        self.prev = None
11        def finder(root):
12            if not root:
13               return 
14            finder(root.left)
15            if self.prev is not None :
16                self.minabsolute = min(self.minabsolute, abs(root.val - self.prev))
17        
18            self.prev = root.val
19            finder(root.right)
20        finder(root)
21        return self.minabsolute
22        
