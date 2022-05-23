a, b, c = map(int, input().split())
if a==b and b==c: print(10000+a*1000)
elif a==b or b==c or c==a:
    temp = [a, b, c]
    temp_ = list({a, b, c})
    for i in temp_:
        temp.remove(i)
    print(1000+temp[0]*100)
else: print(100*max(max(a, b), c))
