
# April 16 2025
# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        k = k % size
        if k == 0:
            return head
        t = (size - k) % size
        end = None
        newhead = None
        temp = head
        count = 0
        while temp:
            count += 1
            if not temp.next:
                end = temp
            if count == t:
                newhead = temp
            temp = temp.next
        end.next = head
        head = newhead.next
        newhead.next = None
        return head