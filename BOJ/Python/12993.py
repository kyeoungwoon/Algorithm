x, y = map(int, input().split())

temp = 0
k = 0
while True:
    temp += 3**k
    if temp == x + y: break
    elif temp > x + y:
        print("0")
        quit()
    k += 1

data = [3**i for i in range(k+1)]
# 1 3 9 27 81 243       91
# if x % 2: # x가 홀수면, 구성요소는 홀수개
temp = x
while True:
    if not temp:
        print("1")
        quit()
    elif temp < 0:
        print("0")
        quit()
    for i in range(len(data)):
        if data[i] > temp: temp -= data.pop(i-1)

    break # TEMP , for sol #2

#2

def find(n):
    i = 0
    while 3**i <= n: i+=1
    return i-1

x, y = map(int, input().split())

sum = x + y
find_sum = find(sum)
sum3 = 0
for i in range(find_sum+1): sum3 += 3**i
if sum != sum3:
    print("0")
    quit()

elmts = [i for i in range(find_sum+1)]
while x:
    find_x = find(x)
    if find_x in elmts: 
        elmts.remove(find_x)
        x -= 3**find_x
    else:
        print("0")
        quit()

print("1")

# review ver.

def find(n):
    i = 0
    while 3**i <= n: i+=1
    return i-1

x, y = map(int, input().split())

sum = x + y
find_sum = find(sum)
sum3 = 0
for i in range(find_sum+1): sum3 += 3**i
print(f"SUM {sum} sum3 {sum3} find_sum {find_sum}") #
if sum != sum3:
    print("0")
    quit()

elmts = [i for i in range(find_sum+1)]
print(f"elmts {elmts}") #
while x:
    find_x = find(x)
    print(f"find_x {find_x}") #
    if find_x in elmts: 
        elmts.remove(find_x)
        x -= 3**find_x
    else:
        print("0")
        quit()
        
print("1")