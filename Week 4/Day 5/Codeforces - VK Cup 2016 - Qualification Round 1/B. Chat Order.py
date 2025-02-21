n = int(input())
name = []
for _ in range(n):
    name.append(input())
ms = set()
for i in range(n - 1,-1 ,-1):
    if name[i] not in ms:
        print(name[i])
        ms.add(name[i])