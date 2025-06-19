# June 19 2025
# https://leetcode.com/problems/course-schedule/description/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        color = [0 for __ in range(numCourses)]
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[0]].append(p[1])

        def helper(current):
            color[current] = 1
            for v in graph[current]:
                if color[v] == 1:
                    return False
                if color[v] == 0:
                    if not helper(v):
                        return False
            color[current] = 2
            return True

        for i in range(numCourses):
            if color[i] == 0:
                if not helper(i):
                    return False
        return True