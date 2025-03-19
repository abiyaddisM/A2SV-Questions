# March 19 2025
# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        if len(s2) > len(s1):
            return False
        dic = {}
        ref = Counter(s2)
        print(ref)
        l = 0
        for r in range(len(s1)):
            dic[s1[r]] = dic.get(s1[r],0) + 1
            if r >= len(s2) - 1:
                for k, v in ref.items():
                    if k not in dic or dic[k] !=  v:
                        break
                else:
                    return True
                dic[s1[l]] -= 1
                l += 1

        return False
