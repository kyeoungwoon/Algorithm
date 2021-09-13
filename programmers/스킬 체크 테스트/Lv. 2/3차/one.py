from itertools import permutations
from math import inf, perm

def solution(A,B):
    answer = inf
    n = len(A)
    for i in list(permutations(B)):
        temp = 0
        for j in range(n):
            temp += A[i]*B[i[j]]
        if answer >= temp:
            answer = temp
    return answer

solution([1,4,2], [5,4,4])
# temp = list(permutations([5, 4, 4]))
# print(temp)