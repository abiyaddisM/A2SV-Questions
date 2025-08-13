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
    size = INT()
    nums = IA()
    dp = {}
    def helper(i, pre):
        if i >= size:
            return 0
        if (i, pre) in dp:
            return dp[(i, pre)]
        include = float('inf')
        if (nums[i] == 3 or nums[i] == 2) and pre != 2: #gym
            include = helper(i + 1, 2)
        if (nums[i] == 3 or nums[i] == 1) and pre != 1: #contest
            include = min(helper(i + 1, 1), include)
        exclude = 1 + helper(i + 1, 0)
        dp[(i, pre)] = min(include, exclude)
        return dp[(i, pre)]
    print(helper(0, 0))

if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    threading.stack_size(2 * 1024 * 1024)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

