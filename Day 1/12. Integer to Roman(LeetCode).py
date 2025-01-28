class Solution:
    def intToRoman(self, num: int) -> str:
        symbolDic = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'
        }
        ma = []
        i = 1
        state = True
        res = ''
        while state:
            state = num % (10 ** i) < num
            ma.append(str(num % (10 ** i) - num % (10 ** (i - 1))))
            i += 1
        for m in reversed(ma):
            s = len(m)
            fir = int(m[0])
            if fir == 4 or fir == 9:
                if fir == 4:
                    res += symbolDic[10 ** (s - 1)]
                    res += symbolDic[5 * 10 ** (s - 1)]
                if fir == 9:
                    res += symbolDic[10 ** (s - 1)]
                    res += symbolDic[10 ** s]

            elif fir < 5:
                res += symbolDic[10 ** (s - 1)] * fir
            elif fir >=5:
                res += symbolDic[5 * 10 ** (s - 1)]
                if fir != 5:
                    res += symbolDic[10 ** (s - 1)] * (fir - 5)


        return res