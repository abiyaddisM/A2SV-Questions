t = int(input())
for _ in range(t):
    n = int(input())
    if n == 2:
        print(1)
        continue
    if n % 4 == 0:
        print(n // 4)
    else:
        print(((n - 2) // 4) + 1)