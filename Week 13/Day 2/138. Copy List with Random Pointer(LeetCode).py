# April 22 2025
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newhead = Node(0)
        dic = {}
        temp = newhead
        while head:
            newnode = Node(head.val)
            if head in dic:
                newnode = dic[head]
            dic[head] = newnode
            temp.next = newnode
            temp = temp.next
            if head.random:
                random = Node(head.random.val)
                if head.random in dic:
                    random = dic[head.random]
                dic[head.random] = random
                temp.random = random
            head = head.next

        return newhead.next