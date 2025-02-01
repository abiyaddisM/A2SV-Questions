n = int(input())
color = input()
count = 0
left = 0
right = 1
while right < n:
    if color[left] != color[right]:
        count += right - left
        left = right
    # if color[left] == color[right]:
    #     count += 1
    # else:
    #     left = right
    right += 1
print(count)
