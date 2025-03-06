# March 6 2025
# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def helper(a,b):
            for k, v in a.items():
                if k not in b or v > b[k]:
                    return False
            return True


        dic = Counter(t)
        tdic = {}
        l = 0
        res = ''
        for r in range(len(s)):
            if s[r] not in dic:
                continue
            tdic[s[r]] = tdic.get(s[r],0) + 1
            while helper(dic,tdic):
                res = res if len(res) < 1 + r - l and res != '' else s[l:r + 1]
                if s[l] in tdic:
                    tdic[s[l]] -= 1
                    if tdic[s[l]] == 0:
                        tdic.pop(s[l])
                l += 1

        return res