from collections import Counter,deque, defaultdict
import math
import sys

def INT():
    return int(sys.stdin.readline())

def IA():
    return list(map(int, sys.stdin.readline().split()))
def STR():
    return sys.stdin.readline()



n, m, k = IA()
mat = []
for _ in range(n):
    temp = STR()
    mat.append(list(temp))
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 'X':
            x, y = i, j
            break
def inbound(i, j):
    return 0 <= i < n and 0 <= j < m
dir = [ (1, 0), (0, -1), (0, 1), (-1, 0)]
dic = ['D',  'L',  'R',  'U']
rev = {'L':'R', 'R':'L', 'U': 'D', 'D': 'U'}
res = ''
level = 0
que = deque([[x, y]])
state = False
state2 = False
for dx, dy in dir:
    cx, cy = dx + x, dy + y
    if inbound(cx, cy) and mat[cx][cy] == '.':
        state2 = True
if not state2:
    print('IMPOSSIBLE')
    exit()

while que:
    if level >= k // 2 or state:
        break
    i, j = que.popleft()
    for l in range(4):
        dx, dy = dir[l]
        cx, cy = i + dx, j + dy
        if inbound(cx, cy) and mat[cx][cy] != '*':
            if res and res[-1] == rev[dic[l]]:
                state = True
            res += dic[l]
            que.append([cx, cy])
            break
    level += 1
if k % 2 != 0:
    print("IMPOSSIBLE")
else:
    temp = []
    for i in range(level):
        temp.append(rev[res[-(i + 1)]])
    temp = ''.join(temp)
    middle = []
    switch = res[-1]
    for _ in range(k - (len(res) + len(temp))):
        middle.append(rev[switch])
        switch = rev[switch]
    middle = ''.join(middle)
    print(res + middle + temp)


