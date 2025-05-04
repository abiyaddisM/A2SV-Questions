# May 4 2025
# https://leetcode.com/problems/remove-nodes-from-linked-list/description/?envType=problem-list-v2&envId=recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def helper(head, pre):
            if not head:
                return 0
            res = helper(head.next, head)
            val = head.val
            if res > val:
                if pre:
                    pre.next = head.next
                    head.next = None
            return max(res, val)

        newHead = ListNode()
        newHead.next = head
        helper(head, newHead)
        return newHead.next
