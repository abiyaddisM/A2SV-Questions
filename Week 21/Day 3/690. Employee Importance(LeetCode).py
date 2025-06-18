# June 18 2025
# https://leetcode.com/problems/employee-importance/description/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, emp: List['Employee'], id: int) -> int:
        self.res = 0
        dic = {}
        visited = set()
        for i in range(len(emp)):
            dic[emp[i].id] = i
        def helper(current, visited):
            if current in visited:
                return
            self.res += emp[dic[current]].importance
            visited.add(current)
            for i in range(len(emp[dic[current]].subordinates)):
                helper(emp[dic[current]].subordinates[i], visited)


        helper(id, visited)
        return self.res