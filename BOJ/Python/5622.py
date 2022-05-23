def est(num):
    if num <= 2: return 3
    elif num <= 5: return 4
    elif num <= 8: return 5
    elif num <= 11: return 6
    elif num <= 14: return 7
    elif num <= 18: return 8
    elif num <= 21: return 9
    elif num <= 25: return 10

ret = 0
for i in input():
    ret += est(ord(i)-ord('A'))
print(ret)