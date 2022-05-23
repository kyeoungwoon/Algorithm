word = input().lower()
# alp = [0 for _ in range(26)]
# for i in word:
#     alp[ord(i)-ord('a')] += 1

dct = dict()
for i in word:
    if i in dct: dct[i] += 1
    else: dct[i] = 1

temp = [k for k, v in dct.items() if v == max(dct.values())]
if len(temp) == 1: print(temp[0].upper()) # ㅋㅋ 대문자로 출력은 좀 ;;
else: print("?")