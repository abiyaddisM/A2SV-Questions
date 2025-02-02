#January 30 2025
#https://www.geeksforgeeks.org/problems/selection-sort/1
class Solution:
    def selectionSort(self, arr):

        for i in range(len(arr)):
            minVal = i
            for j in range(i, len(arr)):
                minVal = minVal if arr[minVal] <= arr[j] else j
            if minVal != i:
                arr[i], arr[minVal] = arr[minVal], arr[i]

        return arr

