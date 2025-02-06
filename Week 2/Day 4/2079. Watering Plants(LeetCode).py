# February 6 2025
# https://leetcode.com/problems/watering-plants/
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        current = capacity
        total = 0
        for i in range(len(plants)):
            current -= plants[i]
            total += 1
            if i + 1 < len(plants) and plants[i + 1] > current:
                total += (i + 1) * 2
                current = capacity
        return total
