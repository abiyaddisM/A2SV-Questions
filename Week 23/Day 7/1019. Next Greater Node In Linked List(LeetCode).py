# July 6 2025
# https://leetcode.com/problems/next-greater-node-in-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nh = ListNode()
        while head:
            temp = head
            head = head.next
            temp.next = nh.next
            nh.next = temp
        res = []
        stack = []
        nh = nh.next
        while nh:
            while stack and stack[-1] <= nh.val:
                stack.pop()
            res.append(stack[-1] if stack else 0)
            stack.append(nh.val)
            nh = nh.next
        res.reverse()
        return res