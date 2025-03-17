# March 17 2025
# https://leetcode.com/problems/duplicate-zeros/?envType=problem-list-v2&envId=two-pointers
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                for j in range(len(arr) - 1,i,-1):
                    arr[j] = arr[j - 1]
                i += 1
            i += 1