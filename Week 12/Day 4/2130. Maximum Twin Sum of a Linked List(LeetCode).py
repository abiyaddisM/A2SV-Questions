# April 17 2025
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        res = 0
        for i in range(len(nums)//2):
            j = -(i + 1)
            res = max(res, nums[i] + nums[j])
        return res