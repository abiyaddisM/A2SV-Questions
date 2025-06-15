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
    res = float('inf')
    nums = INT()
    temp = math.ceil(math.sqrt(nums))
    if (temp * (temp - 1)) >= nums:
        print(temp - 1 + temp - 2)
    else:
        print(temp - 1 + temp - 1)



