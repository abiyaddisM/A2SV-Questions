import sys, threading
from collections import Counter,deque, defaultdict
import heapq
import math
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



def main():
    t = INT()
    nums = IA()
    temp = [0] * max(nums)
    for n in nums:
        temp[n - 1] += 1
    for i in range(len(temp)):
        temp[i] *= (i + 1)
    dic = {}
    def helper(i):
        if i >= len(temp):
            return 0
        if i in dic:
            return dic[i]
        include = temp[i] + helper(i + 2)
        exclude = helper(i + 1)
        dic[i] = max(include, exclude)
        return dic[i] 

    print(helper(0))

if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    threading.stack_size(2 * 1024 * 1024)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


