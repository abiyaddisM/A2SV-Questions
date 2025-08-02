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
    memo = [[-1] * (size + 2) for _ in range(size + 2)]

    def helper(i, pre):
        if i >= size:
            return 0
        if memo[i][pre] != -1:
            return memo[i][pre]
        include = 0
        if pre == -1 or (nums[i] > nums[pre] and math.gcd(nums[i] , nums[pre]) > 1):
            include = 1 + helper(i + 1, i)
        exclude = helper(i + 1, pre)
        memo[i][pre] = max(include, exclude)
        return memo[i][pre]

    print(helper(0, -1))

if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    threading.stack_size(2 * 1024 * 1024)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

