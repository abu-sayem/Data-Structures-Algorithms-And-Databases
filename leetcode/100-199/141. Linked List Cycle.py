# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        store = set()
        if not head:
            return False

        while head.next:
            if head in store:
                return True
            else:
                store.add(head)
                head = head.next
        return False
