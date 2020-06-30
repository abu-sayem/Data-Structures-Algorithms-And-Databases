# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        level = 0
        while queue:
            for i in range(len(queue)):
                temp, level = queue.popleft()
                if not temp.left and not temp.right:
                    return level
                if temp.left:
                    queue.append((temp.left, level+1))
                if temp.right:
                    queue.append((temp.right, level+1))
            level += 1
