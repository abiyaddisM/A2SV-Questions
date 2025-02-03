#February 3 2025
#https://leetcode.com/problems/print-words-vertically/description/
class Solution:
    def printVertically(self, st: str) -> List[str]:
        st = st.split()
        maxs = max(st, key=len)
        res = []
        for i in range(len(maxs)):
            res.append("")
            for s in st:
                if i > len(s) - 1:
                    res[i] += " "
                    continue
                res[i] += s[i]
            j = len(res[i]) - 1
            while j >= 0 and res[i][j] == " ":
                res[i] = res[i][:j]
                j -= 1

        return res
