#February 3 2025
#https://leetcode.com/problems/masking-personal-information/?envType=problem-list-v2&envId=string
class Solution:
    def maskPII(self, st: str) -> str:
        isEmail = False
        for s in st:
            if s == '@':
                isEmail = True
                break
        if isEmail:
            split = st.split('@')
            res = f"{split[0][0].lower()}*****{split[0][-1].lower()}@"
            for s in split[1]:
                res += s.lower()
            return res
        else:
            number = ''
            for s in st:
                if '0' <= s <= '9':
                    number += s
            return ('+' + ('*' * (len(number) - 10)) + '-' if len(number) > 10 else "")  + "***-***-" + number[-4:]