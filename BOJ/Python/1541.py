expr = input()
spl_exprs = expr.split('-')
if len(spl_exprs) > 1: 
    k = int(spl_exprs.pop(0))
    for i in spl_exprs:
        if '+' in i:
            temp = i.split('+')
            temp_ = 0
            for j in temp: temp_ += int(j)
            k -= temp_
        else: k -= int(i)
else:
    addall = list(map(int, spl_exprs[0].split('+')))
    k = 0
    for i in addall: k += i

print(k)

# Trial 2

expr = input().split('-')
tot = 0
if len(expr) == 1:
    temp = expr[0].split('+')
    tot_temp = 0
    for i in temp: tot_temp += int(i)
    tot += tot_temp
else:
    temp = expr.pop(0)
    temp = temp.split('+')
    tot_temp = 0
    for i in temp: tot_temp += int(i)
    tot += tot_temp
    for e in expr:
        if '+' in e:
            temp = e.split('+')
            tot_temp = 0
            for i in temp: tot_temp += int(i)
            tot -= tot_temp
        else:
            tot -= int(e)

# Trial 3
# - 를 기준으로 묶은 다음에 각각 계산해서 빼버리면 되는거 아닌가 ?
# 뒤에 숨겨진 무언가가 또 있는가 ?

def add_all(exp):
    ex = exp.split('+')
    tot = 0
    for e in ex:
        tot += int(e)
    return tot

expr = input().split('-')
tot = add_all(expr.pop(0))
for exp in expr:
    tot -= add_all(exp)
print(tot)