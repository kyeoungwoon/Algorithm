# 부족한 금액 계산하기

def solution(price, money, count):
    need = price*(count*(count+1))/2
    ret = need - money
    if ret >= 0: return ret
    else: return 0

# 숏코딩의 신을 만났습니다

def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

# 지린다,,,