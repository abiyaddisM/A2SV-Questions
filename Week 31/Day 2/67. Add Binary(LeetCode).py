# August 26 2025
# https://leetcode.com/problems/add-binary/description/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def toNumber(x):
            res = 0
            for i in range(len(x)):
                if x[i] == '1':
                    res += 2 ** i
            return res
        def toBin(x):
            if x == 0:
                return '0'
            res = []
            while x > 1:
                if x % 2 == 0:
                    res.append('0')
                else:
                    res.append('1')
                x //= 2
            res.append('1')
            res.reverse()
            return ''.join(res)
        return  toBin(toNumber(a[::-1]) + toNumber(b[::-1]))