# April 20 2025
# https://leetcode.com/problems/reverse-linked-list-ii/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre = None
        front = None
        back = None
        temp = head
        count = 0
        while temp:
            count += 1
            if count == left - 1:
                pre = temp
            if count == left:
                front = temp
            if count == right:
                back = temp
            temp = temp.next
        back2 = back.next
        front2 = front
        back.next = None
        dummy = ListNode()
        for i in range(right - left + 1):
            t1 = dummy.next
            t2 = front
            front = front.next
            dummy.next = t2
            t2.next = t1
        if pre:
            pre.next = dummy.next
        else:
            head = dummy.next
        if front2:
            front2.next = back2
        return head
