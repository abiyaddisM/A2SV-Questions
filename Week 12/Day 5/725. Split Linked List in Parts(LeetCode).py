# April 18 2025
# https://leetcode.com/problems/split-linked-list-in-parts/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        rem = size % k if size >= k else 0
        n = size // k if size >= k else 1
        for i in range(k):
            s = n + (1 if i < rem else 0)
            cur = head
            for _ in range(s - 1):
                if head:
                    head = head.next
            if head:
                t = head
                head = head.next
                t. next = None
            res.append(cur)

        return res