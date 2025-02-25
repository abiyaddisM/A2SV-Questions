# February 25 2025
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        high = arr[-1]
        arr[-1] = -1
        for i in range(2,len(arr) + 1):
            temp = arr[-i]
            arr[-i] = high
            high = max(high,temp)
        return arr
