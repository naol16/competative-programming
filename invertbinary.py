1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if root:
10           rightroot=root.right
11           root.right=root.left
12           root.left=rightroot
13           self.invertTree(root.left)
14           self.invertTree(root.right)
15        return  root
16        
