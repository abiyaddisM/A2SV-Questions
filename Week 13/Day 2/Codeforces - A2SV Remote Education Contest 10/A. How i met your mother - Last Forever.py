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


size = INT()
word = STR()
n = 0
z = 0
for w in word:
    if w == 'n':
        n += 1
    if w == 'z':
        z += 1
print('1 ' * n + '0 ' * z)