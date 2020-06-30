# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)

    def check(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        elif left and right:
            return left.val == right.val and self.check(left.right, right.left) and self.check(left.left, right.right)
        return False


#Iterative solutions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        deque = collections.deque([(root.left, root.right)])
        while deque:
            left, right = deque.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            deque.append((left.left, right.right))
            deque.append((left.right, right.left))
        return True
