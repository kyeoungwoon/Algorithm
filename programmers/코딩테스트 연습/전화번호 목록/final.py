def solution(pb):
    pb.sort()
    for x, y in zip(pb, pb[1:]):
        if y.startswith(x): return False
    return True

# 다른 사람 풀이 - 굳이 ?

def solution(phone_book): 
    for i in range(len(phone_book)): 
        pivot = phone_book[i] 
        for j in range(i+1, len(phone_book)): 
            strlen = min(len(pivot), len(phone_book[j])) 
            if pivot[:strlen] == phone_book[j][:strlen]: 
                return False 
    return True


## 알아가는 것 : int를 sort한게 아니라 string을 sort하였기 떄문에 크기 순으로 나오는 것이 아닌 각 자리의 오름차순(?)으로 정렬되서 나온다.
##              따라서 for문을 2번 겹쳐 써서 O(n^2)를 만드는게 아니라 인접한 것 끼리만 비교해서 O(n)으로 하면 된다.

## P.S.) zip 알아갑니다