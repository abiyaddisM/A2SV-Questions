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

t = INT()
for _ in range(t):
    nums = STR()
    res = 0
    state = True
    while state:
        state = False
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                state = True
                res += 1
                nums = nums[:i] + nums[i + 2:]
                break
    if res % 2 == 0:
        print('NET')
    else:
        print('DA')