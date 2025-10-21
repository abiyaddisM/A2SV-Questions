# October 21 2025
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/
from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        counts = list(freq.values())
        freq_count = Counter(counts)
        items = sorted(freq_count.items())
        if len(items) == 1:
            f, c = items[0]
            return f == 1 or c == 1

        if len(items) == 2:
            (f1, c1), (f2, c2) = items
            if f1 > f2:
                f1, f2 = f2, f1
                c1, c2 = c2, c1

            if f1 == 1 and c1 == 1:
                return True

            if f2 - f1 == 1 and c2 == 1:
                return True

        return False
