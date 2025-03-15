# March 15 2025
# https://leetcode.com/problems/defanging-an-ip-address

class Solution:
    def defangIPaddr(self, add: str) -> str:
        res = ''
        for a in add:
            t = a
            if t == '.':
                t = '[.]'
            res += t
        return res