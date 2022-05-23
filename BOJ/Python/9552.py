# 패턴의 길이 L / 패턴이 지나지 않는점 S
# 첫줄 테스트케이스 수 / 패턴의 길이 & 점들의 수 / 이후 N줄 좌표

t = int(input())
base = []
for x in range(1, 4):
    for y in range(1, 5):
        base.append((x, y))

for _ in range(t):
    valid_pattern = []
    l, s_len = input().split()
    s = []
    for _ in range(s_len):
        x, y = input().split()
        s.append((x, y))
    