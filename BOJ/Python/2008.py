# 세로선 개수, 가로선 개수
# 시점, 종점, 지울 때, 그릴 때
# p ~ p+1 가로선

sero, garo = map(int, input().split())
start, end, erase_cost, draw_cost = map(int, input().split())
garo_list = []
for i in range(garo):
    garo_list.append(int(input()))

# 방법 ? 사다리를 연결
# 무조건 추가해야 하는 경우를 일단 빼고 생각 ?

start_path = [start]
temp = 0
for i in range(len(garo_list)):
    if start_path[-1] == garo_list[i] and i > temp:
        start_path.append(garo_list[i]+1)
        temp = i
    elif start_path[-1] == garo_list[i]+1 and i > temp: 
        start_path.append(garo_list[i])
        temp = i

end_path = [end]
garo_list = garo_list[::-1]
temp = 0
for i in range(len(garo_list)):
    if end_path[-1] == garo_list[i] and i > temp:
        end_path.append(garo_list[i]+1)
        temp = i
    elif end_path[-1] == garo_list[i]+1 and i > temp: 
        end_path.append(garo_list[i])
        temp = i
garo_list = garo_list[::-1]

# print(start_path, end_path

# 무조건 추가해야 하는 경우
gap = 100
if not set(start_path) & set(end_path):
    for i in range(len(start_path)):
        for j in range(len(end_path)):
            gap = min(abs(start_path[i])-end_path[j], gap)
print(gap*draw_cost)

# 섞여 있는 경우



'''

idea !

사다리는 우선 한 칸 씩 밖에 이동하지 못함.
최단경로 ?

'''