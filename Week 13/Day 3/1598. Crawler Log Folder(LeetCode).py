# April 23 2025
# https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            if logs[i] == '../':
                if stack:
                    stack.pop()
            elif logs[i] != './':
                stack.append(0)
        return len(stack)