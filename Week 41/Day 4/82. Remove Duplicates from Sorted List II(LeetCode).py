# November 6 2025
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dic = defaultdict(int)
        cur = head
        while cur:
            dic[cur.val] += 1
            cur = cur.next
        pre = None
        cur = head
        while cur:
            if dic[cur.val] > 1:
                if pre:
                    pre.next = cur.next
                    cur = cur.next
                else:
                    cur = cur.next
                    head = head.next
            else:
                pre = cur
                cur = cur.next
        temp = []
        cur = head
        while cur:
            temp.append(cur.val)
            cur = cur.next
        new_head = ListNode()
        cur = new_head
        for t in temp:
            cur.next = ListNode(t)
            cur = cur.next
        return new_head.next

