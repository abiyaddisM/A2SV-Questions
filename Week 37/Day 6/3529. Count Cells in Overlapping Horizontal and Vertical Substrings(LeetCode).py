# October 11 2025
# https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/description/
class Solution:
    def getLPS(self, s):
        n = len(s)
        LPS = [0]*n
        j = 0
        for i in range(1,n):
            while j>0 and s[i]!=s[j]:
                j = LPS[j-1]
            if s[i]==s[j]:
                j+=1
            LPS[i]=j
        return LPS
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        n, m = len(grid), len(grid[0])
        sz = len(pattern)
        horizontalString = "".join(ch for row in grid for ch in row)
        verticalString = "".join(grid[r][c] for c in range(m) for r in range(n))
        horizontalPatternString = pattern + "#" + horizontalString
        lps1 = self.getLPS(horizontalPatternString)
        verticalPatternString = pattern + "#" + verticalString
        lps2 = self.getLPS(verticalPatternString)
        sz1 = len(lps1)
        scan1 = [0]*(sz1+1)
        for i,v in enumerate(lps1):
            if v==sz:
                scan1[i - sz + 1]+=1
                scan1[i + 1]-=1
        sz2 = len(lps2)
        scan2 = [0]*(sz2+1)
        for i,v in enumerate(lps2):
            if v==sz:
                scan2[i - sz + 1]+=1
                scan2[i + 1]-=1
        visited = [[False]*m for _ in range(n)]
        count1 = 0
        for i in range(sz1):
            count1+=scan1[i]
            if count1>0:
                idx = i - sz - 1
                row = idx//m
                col = idx%m
                if 0<=row<n and 0<=col<m:
                    visited[row][col]=True
        count2 = 0
        ans = 0
        for i in range(sz2):
            count2+=scan2[i]
            if count2>0:
                idx = i - sz - 1
                row = idx%n
                col = idx//n
                if 0<=row<n and 0<=col<m and visited[row][col]:
                    ans+=1
        return ans