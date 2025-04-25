# April 24 2025
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/?envType=problem-list-v2&envId=linked-list
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        while temp:
            if temp.child:
                ed = temp.child
                while ed.next:
                    ed = ed.next
                if temp.next:
                    ed.next = temp.next
                    temp.next.prev = ed
                temp.next = temp.child
                temp.next.prev = temp
            temp.child = None
            temp = temp.next

        return head
