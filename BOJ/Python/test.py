import sys

n = int(sys.stdin.readline().rstrip())
ret = [0 for _ in range(10000)]
for _ in range(n):
    ret[int(sys.stdin.readline().rstrip())-1] += 1
for i in range(len(ret)):
    if ret[i]:
        for j in range(ret[i]): sys.stdout.write(str(i+1)+'\n')