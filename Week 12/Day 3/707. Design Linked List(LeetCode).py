# April 16 2025
# https://leetcode.com/problems/design-linked-list/
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0 or index >= self.getSize():
            return -1
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.addAtHead(val)
            return
        if index > self.getSize():
            return
        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.getSize():
            return
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        temp.next = temp.next.next

    def getSize(self) -> int:
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index, val)
# obj.deleteAtIndex(index)
