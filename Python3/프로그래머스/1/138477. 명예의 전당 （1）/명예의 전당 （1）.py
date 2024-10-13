# k : 명예의 전당 수
# score : 점수 리스트
def solution(k, score):
    top = []
    answer = []
    
    for day in score:
        if len(top) < k:
            top.append(day)
            answer.append(min(top))
            continue

        s = min(top) # 현재 최소 점수  
        if s < day:
            minIdx = top.index(s)        
            del top[minIdx]
            top.append(day)
        answer.append(min(top))
    return answer