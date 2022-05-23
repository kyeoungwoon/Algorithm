def is_group(word):
    temp = []
    for i in range(len(word)):
        if word[i] in temp:
            if word[i-1] != word[i]: return False
        else: temp.append(word[i])
    return True

num = int(input())
ret = 0
for i in range(num):
    if is_group(input()): ret += 1
print(ret)