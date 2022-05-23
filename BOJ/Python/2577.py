ret = [0 for _ in range(10)]
x = 1
for _ in range(3): x *= int(input())
for i in str(x): ret[int(i)]+=1
for i in ret: print(i)