h, m=map(int, input().split())
if(m>=45):
    print(h, m-45)
else:
    m+=15
    if h==0:
        print(23, m)
    else:
        print(h-1, m)