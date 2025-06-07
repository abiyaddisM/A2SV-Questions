# June 7 2025
# https://leetcode.com/problems/fair-distribution-of-cookies/
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        self.res = float('inf')
        def helper(i, bucket):
            if i == len(cookies):
                self.res = min(max(bucket), self.res)
                return
            if max(bucket) >= self.res:
                return
            for j in range(k):
                bucket[j] += cookies[i]
                helper(i + 1, bucket)
                bucket[j] -= cookies[i]


        helper(0, bucket)
        return self.res