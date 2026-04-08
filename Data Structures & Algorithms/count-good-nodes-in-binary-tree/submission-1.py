# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxval):
            lg, rg = 0, 0
            if root.left:
                lg = dfs(root.left, max(root.val, maxval))
            if root.right:
                rg = dfs(root.right, max(root.val, maxval))
            return (lg + rg + 1) if root.val >= maxval else (lg + rg)
        return dfs(root, root.val)
            