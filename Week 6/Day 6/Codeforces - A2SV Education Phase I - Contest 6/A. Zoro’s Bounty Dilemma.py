from collections import Counter
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

t = INT()
for _ in range(t):
    st = STR()
    high, low = 0, 0
    for s in st:
        if s == '>':
            high += 1
        elif s == '<':
            low += 1
    if high == 0 and low == 0:
        print('=')
    elif high == 0:
        print('<')
    elif low == 0:
        print('>')
    else:
        print('?')
