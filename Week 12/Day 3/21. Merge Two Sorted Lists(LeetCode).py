# April 16 2025
# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            if not l1:
                return l2
            return l1
        newhead = ListNode()
        temp = newhead
        while l1 or l2:
            v1 = l1.val if l1 else 101
            v2 = l2.val if l2 else 101
            l0 = 0
            if v1 <= v2:
                l0 = l1
                l1 = l1.next
            else:
                l0 = l2
                l2 = l2.next
            temp.next = l0
            temp = temp.next

        return newhead.next