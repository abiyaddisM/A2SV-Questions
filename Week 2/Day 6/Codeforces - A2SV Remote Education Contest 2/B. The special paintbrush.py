n = int(input())
for _ in range(n):
    size = int(input())
    w = input()
    first = -1
    last = 0
    for i in range(size):
        if first == -1 and w[i] == 'B':
            first = i
        if w[i] == 'B':
            last = i
    if last == -1:
        print(0)
    else:
        print((last - first) + 1)