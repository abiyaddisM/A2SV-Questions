# June 11 2025
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            2 : [1, 3],
            3 : [4, 6],
            4 : [7, 9],
            5 : [10, 12],
            6 : [13, 15],
            7 : [16,19],
            8 : [20, 22],
            9 : [23,26],
        }
        res = []
        def helper(digit, comb, index):
            if index == len(digit):
                if len(comb) > 0:
                    res.append(''.join(comb[:]))
                return
            temp = dic[int(digit[index])]
            for i in range(temp[0], temp[1] + 1):
                c = chr(i + 96)
                comb.append(c)
                helper(digit, comb, index + 1)
                comb.pop()

        helper(digits, [],0)
        return res