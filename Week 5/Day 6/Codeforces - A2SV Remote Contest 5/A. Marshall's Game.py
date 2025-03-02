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

size = INT()
arr = IA()
count = False
for i in arr:
    if i == 1:
        count = True
if count:
    print('HARD')
else:
    print('EASY')
