subj_num = int(input())
scores = list(map(int, input().split()))
M = max(scores)
ret = []
for score in scores:
    ret.append(score/M*100)
tot = 0
for r in ret: tot+=r
print(tot/subj_num)