# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        store = set()
        temp = head
        if not temp:
            return
        while temp.next:
            if temp.next.val == temp.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head


WpXT9BDAvG
