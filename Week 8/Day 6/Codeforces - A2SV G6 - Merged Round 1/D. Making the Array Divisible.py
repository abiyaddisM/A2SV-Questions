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
    size, k = IA()
    nums = IA()
    ext = []

    for n in nums:
        ext.append(n - (n // k) * k)
    dic = Counter(ext)

    ms = set()
    temp = []
    for e in ext:
        if e in ms:
            continue
        temp.append(e)
        ms.add(e)
    temp.sort(reverse=True)

    count = 0
    res = 0
    if 0 in dic:
        dic.pop(0)

    while len(dic) > 0:
        for t in temp:
            if t == 0 or t not in dic:
                continue
            val = k - t
            if res >= val:
                count += 1
                res = 0

            res = val
            dic[t] -= 1
            if dic[t] == 0:
                dic.pop(t)

    res = res + count * k
    print(res + 1 if res > 0 else 0)