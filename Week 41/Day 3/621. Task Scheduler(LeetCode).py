# November 5 2025
# https://leetcode.com/problems/task-scheduler/description/
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks).values()
        maxc = max(counts)
        k = sum(1 for c in counts if c == maxc)
        return max(len(tasks), (maxc - 1) * (n + 1) + k)
