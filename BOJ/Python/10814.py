#1

T  = int(input())

info = {}
for i in range(T):
    age, name = map(str, input().split())
    if age in info.keys():
        info[age] += [name]
    else:
        info[age] = [name]

sorted_age = [int(i) for i in info.keys()]
sorted_age.sort()

for sort_age in sorted_age:
    for name_ in info[str(sort_age)]:
        print(f"{sort_age} {name_}")

#2

T = int(input())

info = []
for i in range(T):
    info.append(input())

info.sort(key=lambda x: int(x[:x.index(" ")]))

for id in info:
    print(id)