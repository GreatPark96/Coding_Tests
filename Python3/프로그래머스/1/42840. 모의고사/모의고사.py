def solution(answers):
    personScore = [[1,2,3,4,5] ,[2,1,2,3,2,4,2,5]  ,[3,3,1,1,2,2,4,4,5,5] ]
    result = [0, 0, 0] 
    
    for k, v in enumerate(personScore):
        for i in range(0, len(answers)):
            if v[i % len(v)] == answers[i]:
                result[k] += 1

    return [person+1 for person, score in enumerate(result) if score == max(result)]
     
            
            
            
