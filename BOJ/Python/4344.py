case_num = int(input())
ret = []
for _ in range(case_num):
    temp = input()
    student_num, scores = int(temp[0]), temp[2:].split()
    avg = 0
    for score in scores: avg += int(score)
    avg /= student_num
    over_avg_student_num = 0
    for score in scores: 
        if int(score) > avg: over_avg_student_num+=1
    ratio = over_avg_student_num / student_num * 100
    ret.append(f"{ratio:.3f}%")

for re in ret: print(re)

# temp 2

case_num = int(input())
for _ in range(case_num):
    scores = list(map(int, input().split()))
    student_num, scores = scores[0], scores[1:]
    avg = 0
    for score in scores: avg += score
    avg /= student_num
    over_avg_student_num = 0
    for score in scores:
        if score > avg: over_avg_student_num += 1
    print(f"{over_avg_student_num / student_num * 100:.3f}%") # 이게 원인인듯 ? 라인별로 안나와서 