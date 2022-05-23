case = int(input())
for _ in range(case):
    graded = input()
    cur = 0
    score = 0
    for i in range(len(graded)):
        if graded[i] == 'O':
            cur+=1
            score+=cur
        else: cur = 0
    print(score)
