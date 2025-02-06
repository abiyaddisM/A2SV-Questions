# February 6 2025
# https://leetcode.com/problems/remove-comments/description/
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        #source = ''.join(source)
        isopen = False
        res = []
        temp = ""
        for sor in source:
            oi = -1
            for i in range(len(sor)):
                if sor[i] == '/':
                    if isopen:
                        if i - 1 > -1 and sor[i - 1] == '*':
                            print(oi)
                            if oi == -1 or i - 1 != oi:
                                isopen = False
                    else:
                        if i + 1 != len(sor) and sor[i + 1] == '/':
                            break
                        elif i + 1 != len(sor) and sor[i + 1] == '*':
                            oi = i + 1
                            isopen = True
                            continue
                        temp += sor[i]
                else:
                    if not isopen:
                        temp += sor[i]
            if temp != '' and not isopen:
                res.append(temp)
                temp = ''


        return res