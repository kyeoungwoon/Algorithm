n = int(input())
a, b = 0, 1
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    for x in range (n-1):
        a, b = b, a+b
    print(b)
