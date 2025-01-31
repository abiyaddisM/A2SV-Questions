#January 31 2025
#https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        temp = []
        r = 0
        l = 0
        while r < len(s):
            while r < len(s) and s[r] == " ":
                r += 1
                l = r
            if r >= len(s):
                break
            while r < len(s) and s[r] != " ":
                r += 1
            temp.append(s[l:r])
            l = r
        print(temp)
        res = ' '.join(temp[::-1])
        return res
