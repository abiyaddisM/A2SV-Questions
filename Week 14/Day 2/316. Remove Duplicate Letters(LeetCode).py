# April 29 2025
# https://leetcode.com/problems/remove-duplicate-letters/description/
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        freq = Counter(s)
        track = set()
        for n in s:
            if n in track:
                freq[n] -= 1
                continue
            while stack and stack[-1] > n and freq[stack[-1]] > 0:
                track.discard(stack.pop())

            track.add(n)
            freq[n] -= 1
            stack.append(n)

        return ''.join(stack)

