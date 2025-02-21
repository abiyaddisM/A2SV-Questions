
def check():
    for i in range(5):
        t = list(map(int, input().split()))
        for j in range(len(t)):
            if t[j] == 1:
                c = abs(i - 2) + abs(j - 2)
                return c


print(check())
