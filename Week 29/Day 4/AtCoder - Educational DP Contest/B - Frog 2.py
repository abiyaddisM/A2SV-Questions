import sys

input = sys.stdin.readline
n, k = map(int, input().split())
h = list(map(int, input().split()))

INF = 10**18
dp = [INF] * n
dp[0] = 0  # cost to stand on stone 0

for j in range(1, n):
    # try all jump lengths up to k (but not past the start)
    for step in range(1, min(k, j) + 1):
        dp[j] = min(dp[j], dp[j - step] + abs(h[j] - h[j - step]))

print(dp[-1])


