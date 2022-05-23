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

n = input()
org = n
k = 0
while True:
    if len(n) == 1:
        n *= 2
    else:
        n = n[1] + str(int(n[0])+int(n[1]))[-1]
    k += 1
    if n == org:
        print(k)
        break


# 26 8 4 2 6
# 55 0 55 
# FAIL - GOOGLED ,,

n = input()
k = 0
if len(n) == 1: n = "0"+n
org = n
while True:
    plus = str((int(n[-2])+int(n[-1]))%10)
    n = n[-1] + plus
    k+=1
    if n == org:
        print(k)
        break

# [-1]을 처리하는 시간이 str의 길이가 길어질 수록 늘어날 것임. 결국엔 배열의 끝까지 보는 것이니
# 간결하게 필요한 것만 남겨놓고 연산하는 것
# 절대적인 연산의 수를 줄이는 것
