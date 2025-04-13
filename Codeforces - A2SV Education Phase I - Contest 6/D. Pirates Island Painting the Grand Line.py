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
    n, m = IA()
    nums = []
    for i in range(n):
        nums.append(IA())
    dic = {}
    ms = set()
    for i in range(n):
        for j in range(m):
            top = nums[i - 1][j] if i > 0 else 0
            bottom = nums[i + 1][j] if i + 1 < n else 0
            left = nums[i][j - 1] if j > 0 else 0
            right = nums[i][j + 1] if j + 1 < m else 0
            k = nums[i][j]
            if top == k or bottom == k or left == k or right == k:
                dic[k] = dic.get(k, 0) + 1
            else:
                ms.add(k)
    for k in ms:
        dic[k] = dic.get(k, 0) + 1
    total = sum(dic.values()) - max(dic.values())
    print(total)