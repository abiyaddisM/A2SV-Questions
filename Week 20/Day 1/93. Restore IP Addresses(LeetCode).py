# June 9 2025
# https://leetcode.com/problems/restore-ip-addresses/
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def check(a):
            return a == str(int(a)) and int(a) < 256
        def helper(points ,index):
            if len(points) == 3:
                if not check(s[points[-1]:]):
                    return
                print(points)
                res.append(
                    s[0:points[0]] + '.' +
                    s[points[0] : points[1]] + '.' +
                    s[points[1] : points[2]] + '.' +
                    s[points[2] : ]
                )
                return
            for i in range(index, len(s)):
                temp = ''
                temp = s[points[-1]: i]
                print(i ,temp)

                if check(temp):
                    points.append(i)
                    helper(points, i + 1)
                    points.pop()

        for i in range(1 ,len(s)):
            if not check(s[:i]):
                continue
            helper([i] ,i + 1)

        return res
