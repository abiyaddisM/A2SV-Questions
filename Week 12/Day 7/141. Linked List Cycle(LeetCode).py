# April 20 2025
# https://leetcode.com/problems/linked-list-cycle/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast:
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            slow = slow.next
            if slow == fast:
                return True
        return False