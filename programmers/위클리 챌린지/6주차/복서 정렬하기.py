from collections import Counter

class Player():
    def __init__(self, kg, record):
        self.kg = kg
        self.record = record

    

def solution(weights, head2head):
    ## weights : 몸무게 리스트
    ## head2head : 전적 / N (None) W (Win) L (Lose)

    ## 전체 승률 > 무거운 사람 이긴 횟수 > 더 무거운 사람 > 작은 번호

    # 전적을 먼저 정리 > how? {1, 2}, W

    ## 일단 정석대로 

    # 전체 승률
    # winrate = []
    # for i in head2head:
    #     temp = Counter(i)
    #     wr = temp['W']+temp['L']
    #     if wr:
    #         winrate.append(0)
    #     else:
    #         winrate.append(float(temp['W']/wr))

    pass