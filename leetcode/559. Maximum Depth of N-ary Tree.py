"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        count = 1
        stack = [root]
        while stack:
            list = []
            while stack:
                node = stack.pop()
                if node.children:
                    #list.append(node.children)
                    list += node.children
            stack = list

            if len(list) > 0:
                count += 1

        return count
                