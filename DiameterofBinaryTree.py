1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    maximumvalue = 0
9
10    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
11        def height(root):
12            if not root:
13               return 0
14            left_side=height(root.left)
15            right_side=height(root.right)
16            self.maximumvalue=max(self.maximumvalue,left_side+right_side)
17            return 1+max(left_side,right_side)
18        height(root)
19        return self.maximumvalue
