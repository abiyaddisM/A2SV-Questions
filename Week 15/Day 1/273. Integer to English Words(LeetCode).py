# May 5 2025
# https://leetcode.com/problems/integer-to-english-words/description/
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        dic = {
                    '0': "Zero",
                    '1': "One",
                    '2': "Two",
                    '3': "Three",
                    '4': "Four",
                    '5': "Five",
                    '6': "Six",
                    '7': "Seven",
                    '8': "Eight",
                    '9': "Nine",
                    '10': "Ten",
                    '11': "Eleven",
                    '12': "Twelve",
                    '13': "Thirteen",
                    '14': "Fourteen",
                    '15': "Fifteen",
                    '16': "Sixteen",
                    '17': "Seventeen",
                    '18': "Eighteen",
                    '19': "Nineteen",
                    '20': "Twenty",
                    '30': "Thirty",
                    '40': "Forty",
                    '50': "Fifty",
                    '60': "Sixty",
                    '70': "Seventy",
                    '80': "Eighty",
                    '90': "Ninety",
                    '100': "Hundred",
                    '1000': "Thousand",
                    '1000000': "Million",
                    '1000000000': "Billion"
                }
        s = str(num)
        temp = []
        ten = 0
        for i in range(len(s)):
            j = -(i + 1)
            ten = int(s[j]) * (10 ** (i % 3)) + ten
            if j % 3 == 0 or -j == len(s):
                temp.append(ten)
                ten = 0
        def helper(n):
            res = ''
            if len(n) == 3:
                return dic[n[0]] + " " + 'Hundred' + " " + helper(n[1:])
            if len(n) == 2:
                if n[0] == '1':
                    return dic[n]
                elif n[0] == '0':
                    return helper(n[1:])
                else:
                    return dic[n[0] + '0'] + " " + helper(n[1:])
            if len(n) == 1:
                if n == '0':
                    return ''
                return dic[n]
        temp2 = []
        for t in temp:
            if t == 0:
                print
                temp2.append('')
                continue
            temp2.append(helper(str(t)))
        print(temp2)
        def helper2(i = 1):
            if i >= len(temp2):
                return
            helper2(i + 1)
            if temp2[i] != '':
                temp2[i] += ' ' + dic[str(10 ** (3 * i))]
        helper2()
        temp3 = ' '.join(reversed(temp2))
        return " ".join(temp3.split())