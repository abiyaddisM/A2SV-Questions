#February 3 2025
#https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'}
        middle = {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'}
        bottom = {'Z', 'X', 'C', 'V', 'B', 'N', 'M'}
        res = []
        for w in words:
            state = -1
            for char in w:
                char = char.upper()
                if char in top:
                    if state != -1 and state != 1:
                        break
                    state = 1
                elif char in middle:
                    if state != -1 and state != 2:
                        break
                    state = 2
                elif char in bottom:
                    if state != -1 and state != 3:
                        break
                    state = 3
            else:
                res.append(w)
        return res
