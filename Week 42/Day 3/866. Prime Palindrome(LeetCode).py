# November 12 2025
# https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory
class Solution:
    def primePalindrome(self, N: int) -> int:
        if N <= 2: return 2
        if N <= 3: return 3
        if N <= 5: return 5
        if N <= 7: return 7
        if 8 <= N <= 11: return 11

        def is_prime(x: int) -> bool:
            if x % 2 == 0 or x % 3 == 0:
                return x in (2, 3)
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i + 2) == 0:
                    return False
                i += 6
            return True

        for left in range(1, 200000):
            s = str(left)
            pal = int(s + s[-2::-1])
            if pal >= N and is_prime(pal):
                return pal

        return -1
