# April 16 2025
# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            total = v1 + v2 + carry
            if total > 9:
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(total % 10)
            temp = temp.next
        if carry:
            temp.next = ListNode(1)

        return head.next