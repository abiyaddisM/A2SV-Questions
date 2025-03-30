from collections import Counter,deque
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
def YesNo(state):
    if state:
        print('YES')
    else:
        print('NO')


def solve(nums):
    size = len(nums)
    l = 1
    r = size - 1
    while l < r:
        if nums[-1] - nums[r - 1] > nums[l]:
            return True
        l += 1
        r -= 1
    return False


t = INT()
for _ in range(t):
    size = INT()
    nums = IA()
    nums.sort()
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    YesNo(solve(nums))