1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    seenbefore=False
9    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
10        if not root:
11           return False
12        if self.dfs(root,subRoot):
13           return True
14        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
15    def dfs(self,root1,root2):
16            if not root1 and not root2:
17               return True
18            if not root1 or not root2 or (root1.val!=root2.val):
19               return False
20            return self.dfs(root1.left,root2.left) and self.dfs(root1.right,root2.right)
21        
22        
