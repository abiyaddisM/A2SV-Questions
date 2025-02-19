# February 19 2025
# https://leetcode.com/problems/gas-station/description/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        fule = 0
        i = 0
        while i < len(gas):
            fule = gas[i]
            j = i
            while fule - cost[j] >= 0:
                fule -= cost[j]
                j = (j + 1) % len(gas)
                fule += gas[j]
                if j == i:
                    return i
            if j < i:
                break
            else:
                i = j + 1
        return -1

