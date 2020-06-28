# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:        
        return self.findleaf(root1, []) == self.findleaf(root2, [])
        
    def findleaf(self, root, leafes):
        if root:
            if not root.left and not root.right:
                leafes.append(root.val)
            self.findleaf(root.left, leafes)
            self.findleaf(root.right, leafes)
        return leafes
            