t = int(input())
def mat(n):
    if n == 1:
        print(1)
        return
    elif n == 2:
        print(-1)
        return
    if n % 2 == 0:
        c = 1
        for i in range(n):
            for j in range(n):
                print(c, end=' ')
                if c == n * n - 1:
                    c = 2
                else:
                    c += 2
            print('')
    else:
        c = 1
        for i in range(n):
            for j in range(n):
                print(c, end=' ')
                if c == n * n:
                    c = 2
                else:
                    c += 2
            print('')



for _ in range(t):
    n = int(input())
    mat(n)

