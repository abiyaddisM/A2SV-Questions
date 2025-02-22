# February 22 2025
# https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        flag = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1] and (not flag):
                flag = 1
            if (i == 0 and arr[i] > arr[i + 1]) or (flag and arr[i] <= arr[i + 1]) or (arr[i] == arr[i + 1]) or (
                    i == len(arr) - 2 and (not flag)):
                return False

        return True