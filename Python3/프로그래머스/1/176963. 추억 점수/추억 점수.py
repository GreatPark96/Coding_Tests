def solution(name, yearning, photo):
    answer = []
    scoreInfo = {}
    
    for i in range(0, len(name)):
        scoreInfo[name[i]] = yearning[i] 
    
    for p in photo:
        score = 0
        
        for target in p:
            score += scoreInfo.get(target, 0)
        answer.append(score)
    return answer