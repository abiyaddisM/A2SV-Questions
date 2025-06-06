# June 6 2025
# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/
class Solution:
    def splitString(self, s: str) -> bool:
        com = []
        def helper(index):
            if index >= len(s):
                return len(com) > 1
            for i in range(index, len(s)):
                val = int(s[index:i + 1])
                if len(com) == 0 or com[-1] == val + 1:
                    com.append(val)
                    if helper(i + 1):
                        return True
                    com.pop()
            return False
        return helper(0)