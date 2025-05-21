# May 21 2025
# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/
class Solution:
    def minMovesToSeat(self, se: List[int], st: List[int]) -> int:
        se.sort()
        st.sort()
        res = 0
        for i in range(len(se)):
            res += abs(se[i] - st[i])
        return res