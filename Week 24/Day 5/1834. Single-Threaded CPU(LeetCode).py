# July 10 2025
# https://leetcode.com/problems/single-threaded-cpu/description/
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i] = (tasks[i][0], tasks[i][1], i)
        heap = []
        tasks = sorted(tasks, key=lambda x: (x[0], x[1], x[2]))
        tasks = deque(tasks)
        temp = tasks.popleft()
        time = temp[0]
        heapq.heappush(heap, (temp[1], temp[2]))
        res = []
        while heap:
            take, i = heapq.heappop(heap)
            time += take
            res.append(i)
            while tasks and tasks[0][0] <= time:
                task = tasks.popleft()
                heapq.heappush(heap, (task[1], task[2]))
            if tasks and not heap:
                task = tasks.popleft()
                time = task[0]
                heapq.heappush(heap, (task[1], task[2]))
        return res

        return res
