h, m = map(int, input().split())
t = int(input())
new_h = h+(m+t)//60
print(f"{(h+(m+t)//60)%24} {(m+t)%60}")
