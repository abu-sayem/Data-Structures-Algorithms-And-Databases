# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        queue = collections.deque([root])
        value = collections.deque()
        while queue:
            list = []
            for i in range(len(queue)):
                temp = queue.popleft()
                list.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            value.appendleft(list)
        return value
