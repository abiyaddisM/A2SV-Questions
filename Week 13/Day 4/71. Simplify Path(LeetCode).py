# April 24 2025
# https://leetcode.com/problems/simplify-path/description/
class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        l = 0
        for r in range(1,len(path)):
            if path[r] == '/' or r + 1 == len(path):
                s = ''
                if path[r] != '/':
                    s = path[l + 1:r + 1]
                else:
                    s = path[l + 1:r]
                if s == '..':
                    if res:
                        res.pop()
                elif s != '.' and s != '':
                    res.append('/'+s)
                l = r
        if not res:
            res.append('/')
        return ''.join(res)