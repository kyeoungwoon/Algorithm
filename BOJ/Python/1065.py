def is_hansoo(num):
    num = str(num)
    num_len = len(num)
    if num_len == 1: return True
    else:
        temp = int(num[1]) - int(num[0])
        for i in range(num_len-1):
            if int(num[i+1]) - int(num[i]) != temp: return False
        return True


lim = int(input())
ret = 0
for i in range(1, lim+1):
    if is_hansoo(i): ret += 1
print(ret)

