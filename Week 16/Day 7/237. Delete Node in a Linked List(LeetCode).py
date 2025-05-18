# May 18 2025
# https://leetcode.com/problems/delete-node-in-a-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        while node.next.next:
            val = node.next.val
            node.next.val = node.val
            node.val = val
            node = node.next
        val = node.next.val
        node.next.val = node.val
        node.val = val
        node.next = None
