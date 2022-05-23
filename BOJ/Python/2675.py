num = int(input())
for _ in range(num):
    n, word = input().split()
    temp = ''
    for i in word:
        temp += i*int(n)
    print(temp)