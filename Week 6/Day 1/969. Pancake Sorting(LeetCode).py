# March 3 2025
# https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)):
            maxs = 0
            for j in range(len(arr) - i):
                maxs = j if arr[j] > arr[maxs] else maxs
            if maxs + 1 == len(arr) - i:
                continue
            if maxs != 0:
                res.append(maxs + 1)
            for j in range((maxs + 1)//2):
                arr[j],arr[maxs] = arr[maxs],arr[j]
                maxs -= 1
            res.append(len(arr)- i)
            temp = arr[len(arr) - i - 1::-1]
            temp.extend(arr[len(arr) - i:])
            arr = temp
        return res