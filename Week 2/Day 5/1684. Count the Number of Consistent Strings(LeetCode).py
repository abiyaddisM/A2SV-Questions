# February 7 2025
# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        myset = set(allowed)
        count = 0
        for word in words:

            for w in word:
                if w not in myset:
                    break
            else:
                count += 1
        return count