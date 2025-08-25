# August 25 2025
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/
from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dic = [0 for _ in range(26)]
        dic[ord(s[0]) - 97] = 1
        count = 1

        for i in range(1, len(s)):
            if ((ord(s[i]) - ord(s[i - 1])) == 1) or (s[i] == 'a' and s[i - 1] == 'z'):
                count += 1
            else:
                count = 1
            dic[ord(s[i]) - 97] = max(dic[ord(s[i]) - 97], count)
        print(sum(dic))
        return sum(dic)