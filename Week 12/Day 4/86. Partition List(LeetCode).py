# April 17 2025
# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        gh = ListNode()
        lh = ListNode()
        gtemp = gh
        ltemp = lh
        while head:
            if head.val < x:
                t = head
                head = head.next
                t.next = None
                ltemp.next = t
                ltemp = ltemp.next
            else:
                t = head
                head = head.next
                gtemp.next = t
                t.next = None
                gtemp = gtemp.next

        ltemp.next = gh.next
        return lh.next