n = int(input())
ret = []
for _ in range(n):
    ret.append(int(input()))
ret.sort()
for i in ret: print(i)

#2

n = int(input())
ret = [0 for _ in range(10000)]
for _ in range(n):
    ret[int(input())-1] += 1
for i in range(len(ret)):
    if not ret[i]:
        for j in range(ret[i]): print(i+1)

#3

import sys

n = int(sys.stdin.readline().rstrip())
ret = [0 for _ in range(10000)]
for _ in range(n):
    ret[int(sys.stdin.readline().rstrip())-1] += 1
for i in range(len(ret)):
    if ret[i]:
        for j in range(ret[i]): sys.stdout.write(str(i+1)+'\n')