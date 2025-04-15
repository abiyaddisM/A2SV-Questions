# April 15 2025
# https://leetcode.com/problems/remove-linked-list-elements/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        pre = head
        temp = head.next
        while temp:
            if temp.val == val:
                pre.next = temp.next
                temp.next = None
                temp = pre.next
            else:
                temp = temp.next
                pre = pre.next

        return head