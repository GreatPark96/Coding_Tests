def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    
    box = []
    boxCnt = int(len(score) / m)
    
    for i in range(0, len(score), m):
        if len(score[i:i+m]) == m:
            box.append(score[i:i+m])
    for j in range(0, len(box)):
        answer += min(box[j]) * m
    return answer
    
    