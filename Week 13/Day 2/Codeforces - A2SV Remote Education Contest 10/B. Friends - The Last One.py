from collections import Counter, deque
import math


def INT():
    return int(input())


def IA():
    return list(map(int, input().strip().split()))


def SA():
    return input().split()


def STR():
    return input()


def PA(arr):
    print(' '.join(map(str, arr)))


def YesNo(state):
    if state:
        print('YES')
    else:
        print('NO')




t = INT()
for _ in range(t):
    n, m = IA()

    nums = IA()
    nums.sort()
    l = (nums[0] * 2 + 1) // 2
    r = 0
    state = True
    for i in range(n):
        val = nums[i] * 2 + 1
        if m - (val - r) >= 0:
            m = m - (val - r)
            r = (nums[i] * 2 + 1) // 2
        else:
            if m - (val - (r + l)) >= 0:
                m = m - (val - (r + l))
                l = 0
                r = 0
            else:
                state = False
    YesNo(state)