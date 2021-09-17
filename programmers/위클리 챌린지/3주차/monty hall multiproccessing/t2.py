import time

st = time.time()

for _ in range(99999999):
    pass

print(time.time()-st)