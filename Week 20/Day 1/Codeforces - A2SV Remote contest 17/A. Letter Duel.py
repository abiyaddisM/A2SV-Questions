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
    size = INT()
    nums = STR()
    def solv():
        for i in range(size - 1):
            if nums[i] != nums[i + 1]:
                return [i + 1,i + 2]
        return [-1,-1]
    PA(solv())
