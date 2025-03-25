# March 25 2025
# https://leetcode.com/problems/compare-version-numbers/description/
class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1_parts = list(map(int, v1.split('.')))
        v2_parts = list(map(int, v2.split('.')))
        max_length = max(len(v1_parts), len(v2_parts))

        for i in range(max_length):
            num1 = v1_parts[i] if i < len(v1_parts) else 0
            num2 = v2_parts[i] if i < len(v2_parts) else 0
            if num1 > num2:
                return 1
            if num1 < num2:
                return -1
        return 0
