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
    dic = Counter(nums)
    if len(dic) == 1:
        print('NO')
        continue
    res = []
    skip = -1
    for i in range(size):
        if i == skip:
            continue
        for j in range(size):
            if nums[i] != nums[j]:
                if skip == -1:
                    skip = j
                res.append([i + 1, j + 1])
                break
    print('YES')
    for r in res:
        PA(r)
