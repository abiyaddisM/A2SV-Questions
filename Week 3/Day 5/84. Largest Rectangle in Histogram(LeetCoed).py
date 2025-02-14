# February 14 2025
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def check(h):
            st = []
            left = [0 for _ in range(len(h))]
            for i in range(len(h)):
                count = 0
                while st and st[-1][0] >= h[i]:
                    ind = st[-1][1]
                    count += left[ind] + 1
                    st.pop()
                st.append([h[i],i])
                left[i] = count
            return left
        l = check(heights)
        r = check(heights[::-1])[::-1]
        maxs = 0
        for i in range(len(heights)):
            maxs = max(heights[i] * (l[i] + r[i] + 1),maxs)

        return maxs


