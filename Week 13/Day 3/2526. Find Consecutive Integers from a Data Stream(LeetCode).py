# April 23 2025
# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.queue = deque()

    def consec(self, num: int) -> bool:
        if num == self.val:
            if len(self.queue) < self.k:
                self.queue.append(num)
        else:
            self.queue = deque()
        return len(self.queue) == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)