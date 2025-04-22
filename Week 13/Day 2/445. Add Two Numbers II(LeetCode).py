# April 22 2025
# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper(l1, l2, count):
            if not l1 or not l2:
                return 0
            if count > 0:
                rem = helper(l1.next, l2, count - 1)
                total = l1.val + rem
                l1.val = total % 10
                return int(total > 9)
            else:
                rem = helper(l1.next, l2.next, count - 1)
                total = l1.val + l2.val + rem
                l1.val = total % 10
                return int(total > 9)
        def size(head):
            size = 0
            while head:
                head = head.next
                size += 1
            return size
        s1 = size(l1)
        s2 = size(l2)
        if s1 >= s2:
            rem = helper(l1, l2, s1 - s2)
            if rem:
                temp = ListNode(1)
                temp.next = l1
                return temp
            return l1
        else:
            rem = helper(l2, l1, s2 - s1)
            if rem:
                temp = ListNode(1)
                temp.next = l2
                return temp
            return l2