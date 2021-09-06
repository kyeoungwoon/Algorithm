def solution(A,B):
    answer = 0
    n = len(A)
    A.sort()
    B.sort()
    for i in range(n):
        answer += A[i]*B[-i-1]
    return answer

## 하지만 이게 왜 답인지는 모름 ㅋㅋ