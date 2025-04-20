# April 20 2025
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        l = head
        r = head.next
        while r and l:
            t1 = l
            t2 = r
            l = l.next
            l = l.next
            r = r.next
            if r:
                r = r.next
            t1.next = t2.next
            t2.next = t1
            temp.next = t2
            temp = temp.next
            temp = temp.next
        return dummy.next

