# April 16 2025
# https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        t = math.floor(count / 2)
        for _ in range(t):
            head = head.next


        return head