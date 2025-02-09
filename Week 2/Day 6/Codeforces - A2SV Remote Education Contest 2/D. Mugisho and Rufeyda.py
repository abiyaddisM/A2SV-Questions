n, t = map(int,input().split())

if t == 10:
    if n == 1:
        print(-1)
    else:
        print(10 ** (n - 1))
else:
    print(10 ** (n - 1) * t)