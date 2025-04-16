# April 16 2025
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        if n == size:
            return head.next
        t = size - n
        temp = head
        for _ in range(t -1):
            temp = temp.next
        t = temp.next
        temp.next = t.next
        t.next = None

        return head