t = int(input())
size, k = map(int,input().split())
for _ in range(t):
    li = list(map(int,input().split()))
    po = list(map(int,input().split()))
    tt = 0
    for l in li:
        tt += l
    c = 0
    m = 0
    for i in range(len(po)):
        m = i if abs(po[i]) < abs(po[m]) else m
    left = m - 1
    right = m + 1
    b = k
    for _ in range(len(po)):
        