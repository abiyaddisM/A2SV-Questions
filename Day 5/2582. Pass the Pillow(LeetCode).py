#January 31 2025
#https://leetcode.com/problems/pass-the-pillow/
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return time + 1
        elif time == n:
            return n - 1
        ispositive = True
        while time >= n:
            ispositive = not ispositive
            time = time - (n - 1)
        if ispositive:
            return time + 1
        else:
            return n - time
