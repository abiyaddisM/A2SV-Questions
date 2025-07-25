# July 20 2025
# https://leetcode.com/problems/previous-permutation-with-one-swap/description/
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                max_j = i + 1
                for j in range(i + 1, n):
                    if arr[j] < arr[i] and arr[j] > arr[max_j]:
                        max_j = j
                arr[i], arr[max_j] = arr[max_j], arr[i]
                break
        return arr
