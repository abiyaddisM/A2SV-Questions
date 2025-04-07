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


s = STR()
res = 0
dic = {}
l = 0
for r in range(len(s)):
    dic[s[r]] = dic.get(s[r], 0) + 1
    if len(dic) == 3:
        res += l
    while len(dic) == 3:
        res += 1
        dic[s[l]] -= 1
        if dic[s[l]] == 0:
            dic.pop(s[l])
        l += 1

print(res)