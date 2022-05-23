temp = []
n = int(input())
for i in range(n):
    temp.append(int(input()))
temp.sort()
for i in temp:
    print(i)


# Trial 2

import sys

def quick_sort(array, start, end):
    if start >= end: return # 원소가 1개인 경우
    pivot = array[start] # 피벗은 첫 요소
    left, right = start + 1, end
    
    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈린 경우
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않은 경우
            array[right], array[left] = array[left], array[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

l = []
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    l.append(int(sys.stdin.readline().rstrip()))
quick_sort(l, 0, len(l)-1) # sort 쓰고 passed
for i in l:
    sys.stdout.write(str(i)+'\n')
