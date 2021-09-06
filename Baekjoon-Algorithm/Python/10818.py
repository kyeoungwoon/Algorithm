# case = int(input())
# a,b,c,d,e = map(int, input().split())
# l = [a,b,c,d,e]
# l.sort()
# print(f"{l[0]} {l[-1]}")

# l = list()
# for i in range(int(input())):
#     l.append(map(int, input().split()))
# l.sort()
# print(l[0], l[-1])

case = int(input())
l = list(map(int, input().split()))
print(min(l), max(l))
