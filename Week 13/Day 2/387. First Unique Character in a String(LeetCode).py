# April 22 2025
# https://leetcode.com/problems/first-unique-character-in-a-string/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        q = deque()
        dic = {}
        res = 0
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1
            while q and dic[s[q[0]]] > 1:
                q.popleft()
            if dic[s[i]] == 1:
                q.append(i)
        return q[0] if q else -1