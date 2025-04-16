# April 16 2025
# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = ListNode()
        while head:
            temp = newhead.next
            newhead.next = head
            head = head.next
            newhead.next.next = temp
        return newhead.next