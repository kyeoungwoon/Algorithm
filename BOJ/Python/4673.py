table = set()
for i in range(1, 10000):
    d = i
    for j in str(i): d += int(j)
    table.add(d)
for i in range(1, 10001):
    if i not in table: print(i)