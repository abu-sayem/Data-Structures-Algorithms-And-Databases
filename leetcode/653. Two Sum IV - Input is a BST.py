# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        store = set()
        list = [root]
        while list:
            temp = list.pop()
            if temp.val in store:
                return True
            store.add(k-temp.val)
            if temp.left:
                list.append(temp.left)
            if temp.right:
                list.append(temp.right)
        return False
