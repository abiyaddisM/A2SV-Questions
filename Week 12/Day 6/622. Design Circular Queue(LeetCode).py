# April 19 2025
# https://leetcode.com/problems/design-circular-queue/description/
class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.head = ListNode()
        self.tail = self.head
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.k == self.size:
            return False
        self.size += 1
        self.tail.next = ListNode(value)
        self.tail = self.tail.next
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        elif self.size == 1:
            self.tail = self.head
        t = self.head.next
        self.head.next = t.next
        t.next = None
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.next.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()