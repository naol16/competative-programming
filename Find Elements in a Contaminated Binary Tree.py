# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
      
    def __init__(self, root: Optional[TreeNode],x=0):
        self.exist=set()
        def dfs(node,val):
            if not node:
               return None
            node.val=val
            self.exist.add(node.val)
            dfs(node.left,node.val*2+1)
            dfs(node.right,node.val*2+2)
        dfs(root,0)

    def find(self, target: int) -> bool:
        if target in self.exist:
           return True
        else:
             return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
