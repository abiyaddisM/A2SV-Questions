# April 25 2025
# https://leetcode.com/problems/decode-string/description/
class Solution:
    def decodeString(self, arr: str) -> str:
        nums = ''
        letter = ''
        stack = []
        for s in arr:
            if '0' <= s <= '9':
                nums += s
                continue
            if 'a' <= s <= 'z':
                letter += s
                continue
            if s == '[':
                if letter != '':
                    stack.append(letter)
                    letter = ''
                stack.append(int(nums))
                nums = ''
                continue

            while isinstance(stack[-1], str):
                letter = stack.pop() + letter
            stack.append(letter * stack.pop())
            letter = ''
        res = ''
        print(stack)
        for s in stack:
            res += s
        res += letter
        return res
