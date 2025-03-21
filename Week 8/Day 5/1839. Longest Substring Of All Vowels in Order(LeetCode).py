# March 21 2025
# https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/description/
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        dic = {
            1: 'a',
            2: 'e',
            3: 'i',
            4: 'o',
            5: 'u'
        }
        res = 0
        st = " "
        cur = 1
        l = 0
        for r in range(len(word)):
            if word[r] == st[-1]:
                pass
            elif cur in dic and word[r] == dic[cur]:
                st += word[r]
                cur += 1
            else:
                if word[r] == 'a':
                    st = " a"
                    cur = 2
                    l = r
                else:
                    st = " "
                    cur = 1
                    l = r + 1
            if st == ' aeiou':
                res = max(res,r - l + 1)
        return res