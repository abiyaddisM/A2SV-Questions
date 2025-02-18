t = int(input())
for _ in range(t):
    size = int(input())
    nums = list(map(int,input().strip().split()))
    count = 0
    def helper(a):
        if len(a) == 1:
            return [a,0]

        b = helper(a[0:len(a) // 2])
        c = helper(a[len(a) // 2: len(a)])
        if b[1] == -1 or c[1] == -1:
            return [[], -1]
        if b[0][0] > c[0][-1]:
            if b[0][0] - 1 != c[0][-1]:
                return [[], -1]
            c[0].extend(b[0])
            c[1] += 1 + b[1]
            return c
        else:
            if b[0][-1] + 1 != c[0][0]:
                return [[], -1]
            b[0].extend(c[0])
            b[1] += c[1]
            return b

    print(helper(nums)[1])