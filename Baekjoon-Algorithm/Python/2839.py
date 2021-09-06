# https://www.acmicpc.net/problem/2839

quan = int(input())
n=0
while True:

    if quan < quan%5 + 5*n:
        print(-1)
        break

    elif (quan%5 + 5*n) % 3 == 0:
        print(quan//5 - n + (quan%5 + 5*n) // 3)
        break

    n += 1