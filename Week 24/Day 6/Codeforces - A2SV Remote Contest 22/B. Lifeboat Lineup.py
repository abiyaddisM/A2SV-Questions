from collections import Counter,deque, defaultdict
import heapq
import math
import sys

def INT():
    return int(sys.stdin.readline())

def IA():
    return list(map(int, sys.stdin.readline().split()))
def SA():
    return input().split()
def STR():
    return sys.stdin.readline()
def PA(arr):
    print(' '.join(map(str, arr)))
def YesNo(state):
    if state:
        print('YES')
    else:
        print('NO')

size = INT()
heap = []
dic = {'rat':1, 'woman':2, 'child':2,'man':3 ,'captain':4,}
for i in range(size):
    name, pos = input().split()
    heapq.heappush(heap, (dic[pos], i, name))
while heap:
    _, _, name = heapq.heappop(heap)
    print(name)