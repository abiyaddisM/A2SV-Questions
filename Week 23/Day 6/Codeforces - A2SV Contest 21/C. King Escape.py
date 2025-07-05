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

n = INT()
qx, qy = IA()
kx, ky = IA()
cx, cy = IA()
res = True
if not ((kx > qx and cx > qx) or (kx < qx and cx < qx)):
    res = False
if not ((ky > qy and cy > qy) or (ky < qy and cy < qy)):
    res = False



YesNo(res)