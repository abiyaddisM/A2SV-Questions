# June 13 2025
# https://leetcode.com/problems/expression-add-operators/description/?roomId=uUkzjU
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def check(val):
            return len(val) > 1 and val[0] == '0'

        def helper(idx, path, total, prev):
            if idx == len(num):
                if total == target:
                    res.append(path[:])
                return
            for i in range(idx, len(num)):
                newPath = num[idx: i + 1]
                curr = int(newPath)
                if check(newPath):
                    break
                if idx == 0:
                    helper(i + 1, newPath, curr, curr)
                else:
                    helper(i + 1, path + '+' + newPath, total + curr, curr)
                    helper(i + 1, path + '-' + newPath, total - curr, -curr)
                    helper(i + 1, path + '*' + newPath, total - prev + prev * curr, curr * prev)

        helper(0, '', 0, 0)
        return res        