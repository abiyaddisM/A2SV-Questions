# April 11 2025
# https://leetcode.com/problems/car-fleet/description/

class Solution:
    def carFleet(self, t: int, p: List[int], s: List[int]) -> int:
        temp = [[p[i], s[i]] for i in range(len(p))]
        temp.sort(key = lambda x: x[0], reverse = True)
        stack = []
        res = 0
        for i in range(len(p)):

            while stack and stack[-1][1] > temp[i][1]:
                stack.pop()
                if not stack:
                    res += 1
            if stack:
                l = (t - stack[0][0]) / stack[0][1]
                r = (t - temp[i][0]) / temp[i][1]
                # print(l,r)
                if l < r:
                    res += 1
                    stack = []
            stack.append(temp[i])
        res += 1
        return res