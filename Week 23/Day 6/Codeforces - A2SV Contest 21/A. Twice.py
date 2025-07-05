from collections import Counter,deque, defaultdict
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
    nums = IA()
    dic = defaultdict(int)
    for i in range(size):
        dic[nums[i]] += 1
    res = 0
    for k, v in dic.items():
        res += v // 2
    print(res)
