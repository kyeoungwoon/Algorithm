n = input()
org = n

k = 1
while True:
    ne = 0
    for i in n: ne += int(i)
    n = n[-1]+str(ne)[-1]
    if org == n:
        print(k)
        break
    else: k+=1
