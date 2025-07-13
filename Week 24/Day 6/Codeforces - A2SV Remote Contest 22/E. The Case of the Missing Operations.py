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
res = []
heap = []
for _ in range(size):
    temp = SA()
    if temp[0] == 'insert':
        val = int(temp[1])
        heapq.heappush(heap, val)
        res.append(f'insert {val}')
    elif temp[0] == 'getMin':
        val = int(temp[1])
        while heap and heap[0] < val:
            heapq.heappop(heap)
            res.append('removeMin')
        if not heap or heap[0] > val:
            heapq.heappush(heap, val)
            res.append(f'insert {val}')
        res.append(f'getMin {val}')
    elif temp[0] == 'removeMin':
        if not heap:
            res.append('insert 0')
        else:
            heapq.heappop(heap)
        res.append('removeMin')

print(len(res))
for r in res:
    print(r)