cvrt = input()
i = 0
ret = 0
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
while i < len(cvrt):
    if cvrt[i:i+2] in croatia:
        # print(cvrt[i:i+2])
        ret += 1
        i += 2
    else:
        # print(cvrt[i])
        ret += 1
        i += 1
print(ret)

#2

croatic = input()
converted = 0
for i in range(1, len(croatic)):
    if croatic[i] in ['=', '-']:
        if i >= 2:
            if croatic[i-2:i] == 'dz': converted += 1
        converted += 1
    
    if croatic[i] == 'j':
        if croatic[i-1] in ['l', 'n']: converted += 1
print(len(croatic) - converted)