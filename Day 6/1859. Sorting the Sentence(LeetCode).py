#Febuary 1 2025
#https://leetcode.com/problems/sorting-the-sentence/description/
class Solution:
    def sortSentence(self, st: str) -> str:
        split = st.split()
        res = ''
        for i in range(len(split)):
            for s in split:
                if s[-1] == str(i + 1):
                    res += s[:len(s) - 1]
                    res += " " if i < len(split) - 1 else ""
                    break
        return res
