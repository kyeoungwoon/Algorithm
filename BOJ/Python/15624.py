#runtime error

def Fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

N = int(input())
print(Fibonacci(N)%1000000007)

fibo=[0,1]
n = int(input())
if(n==0):
    print(0)
elif(n==1):
    print(1)
else:
    for x in range(n-3):
        fibo.append(fibo[x]+fibo[x+1])
    print(fibo[n])

#time over
fibo=[0,1]
n = int(input())
if(n==0):
    print(0)
elif(n==1):
    print(1)
else:
    for x in range(n-1):
        temp=fibo[0]+fibo[1]
        fibo[0]=fibo[1]
        fibo[1]=temp
    print(fibo[1])

#memory over
fibo=[0,1]
n = int(input())
if(n==0):
    print(0)
elif(n==1):
    print(1)
else:
    for x in range(n-3):
        fibo.append(fibo[x]+fibo[x+1])
    print(fibo[n])

#timeout
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


# 행렬을 이용한 코드

def matrix(carr, arr):
    carr = [carr[0]*arr[0] + carr[1]*arr[2], carr[0]*arr[1] + carr[1]*arr[3], \
            carr[2]*arr[0] + carr[3]*arr[2], carr[2]*arr[1] + carr[3]*arr[3]]
    return carr
        
carr = [1,1,1,0]
arr = [1,1,1,0]

n = int(input())

for x in range(n-1):
    carr = matrix(carr, arr)

print(carr[2])