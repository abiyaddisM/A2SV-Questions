from collections import Counter
import math
def INT():
    return int(input())
def IA():
    return list(map(int,input().strip().split()))
def SA():
    return input().split()
def STR():
    return input()
def PA(arr):
    print(' '.join(map(str, arr)))

t = INT()
for _ in range(t):
    n = INT()
    nums = IA()
    count = 0
    l = 0
    for r in range(n):
        if l != 0 and r != n - 1:
            if nums[l - 1] > nums[l] and nums[r + 1] > nums[r]:
                count += 1
        else:
            if (l == 0 and r == n - 1) or (l == 0 and nums[r + 1] > nums[r]) or (l != 0 and nums[l - 1] > nums[l]):
                count += 1
        if r != n - 1 and nums[r + 1] != nums[r]:
            l = r + 1

    if count == 1:
        print('YES')
    else:
        print('NO')
