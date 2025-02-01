word1 = input()
word2 = input()
for i in range(len(word1)):
    if word1[i].upper() > word2[i].upper():
        print(1)
        break
    elif word1[i].upper() < word2[i].upper():
        print(-1)
        break
else:
    print(0)
