test = int(input())
for test_round in range(test):
    target = list(input().strip())
    len_target = len(target)
    iter_count = int(input())

    count = 0
    for j in range(len_target - 3):
        if target[j] == '1' and target[j + 1] == '1' and target[j + 2] == '0' and target[j + 3] == '0':
            count += 1

    for round in range(iter_count):
        i, q = input().split()
        i = int(i) - 1

        if target[i] == q:
            print("YES" if count > 0 else "NO")
            continue

        for j in range(max(0, i - 3), min(i + 1, len_target - 3)):
            if target[j] == '1' and target[j + 1] == '1' and target[j + 2] == '0' and target[j + 3] == '0':
                count -= 1

        target[i] = q

        for j in range(max(0, i - 3), min(i + 1, len_target - 3)):
            if target[j] == '1' and target[j + 1] == '1' and target[j + 2] == '0' and target[j + 3] == '0':
                count += 1

        print("YES" if count > 0 else "NO")