# April 17 2025
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ms = set()
        ms.add(head.val)
        temp = head.next
        pre = head
        while temp:
            if temp.val in ms:
                t = temp
                pre.next = t.next
                temp = temp.next
                t.next = None
            else:
                ms.add(temp.val)
                pre = pre.next
                temp = temp.next

        return head