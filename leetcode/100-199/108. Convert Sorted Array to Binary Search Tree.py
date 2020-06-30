# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        temp = len(nums) // 2
        node = TreeNode(nums[temp])
        node.left = self.sortedArrayToBST(nums[:temp])
        node.right = self.sortedArrayToBST(nums[temp+1:])
        return node
        
        
        