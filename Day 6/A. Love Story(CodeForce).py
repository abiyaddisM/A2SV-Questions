n = int(input())
for _ in range(n):
    count = 0
    phrase = input()
    compare = "codeforces"
    for i in range(10):
        if phrase[i] != compare[i]:
            count += 1
    print(count)
