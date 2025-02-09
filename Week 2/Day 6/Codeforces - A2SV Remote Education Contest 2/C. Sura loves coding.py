n = int(input())
w = input()
res = []
for i in range(n):
    if n % 2 == 0:
        if i % 2 != 0:
            res.append(w[i])
        else:
            res.insert(0,w[i])
    else:
        if i % 2 == 0:
            res.append(w[i])
        else:
            res.insert(0,w[i])
print(''.join(res))
