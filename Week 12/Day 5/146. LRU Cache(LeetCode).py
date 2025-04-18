# April 18 2025
# https://leetcode.com/problems/lru-cache/description/
class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_end(self, node):
        """Add node before tail (most recent)."""
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_end(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove from front (least recently used)
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]

            # Add new node
            new_node = ListNode(key, value)
            self._add_to_end(new_node)
            self.cache[key] = new_node
