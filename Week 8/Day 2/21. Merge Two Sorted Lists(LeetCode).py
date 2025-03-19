# March 18 2025
# https://leetcode.com/problems/merge-two-sorted-lists/description/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        temp = ListNode()
        res = temp
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            while list1:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
        if list2:
            while list2:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
        return res.next

