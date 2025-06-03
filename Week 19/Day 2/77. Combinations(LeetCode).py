# June 3 2025
# https://leetcode.com/problems/combinations/description/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def helper(start = 0, arr = []):
            print(arr)
            if len(arr) == k:
                res.append(arr[:])
                return
            for i in range(start + 1,n + 1):
                arr.append(i)
                helper(i,arr)
                arr.pop()
        helper()
        return res