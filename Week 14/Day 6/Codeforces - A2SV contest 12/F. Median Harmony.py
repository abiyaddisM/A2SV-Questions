from collections import defaultdict

def count_good_subarrays(n, a):
    total_subarrays = n * (n + 1) // 2
    bad_subarrays = 0

    for x in range(1, 11):
        b = [0] * (n + 1)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            b[i] = 1 if a[i - 1] <= x else -1
            prefix_sum[i] = prefix_sum[i - 1] + b[i]

        count = defaultdict(int)
        k = 0
        for i in range(1, n + 1):
            if a[i - 1] == x:
                while k < i:
                    count[prefix_sum[k]] += 1
                    k += 1
            bad_subarrays += count[prefix_sum[i]]

    return total_subarrays - bad_subarrays

# Example usage:
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(count_good_subarrays(n, a))
