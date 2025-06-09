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

a = STR()
b = STR()
res = []
pos = 0
for n in a:
    pos += 1 if n == '+' else -1
def helper(sum, i):
    if i == len(b):
        res.append(sum)
        return
    if b[i] != '?':
        sum += 1 if b[i] == '+' else -1
        helper(sum, i + 1)
    else:
        helper(sum + 1, i + 1)
        helper(sum - 1, i + 1)

helper(0, 0)
count = 0
for r in res:
    if r == pos:
        count += 1
print(count/len(res))