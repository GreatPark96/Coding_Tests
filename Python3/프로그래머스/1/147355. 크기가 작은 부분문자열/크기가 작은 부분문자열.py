def solution(t, p):
    answer = 0
    sliceList = []
    
    for i in range(0, len(t)):
        if(i + len(p) <= len(t)): 
            sliceList.append(t[i:i+len(p)])

    for num in sliceList:
        if int(num) <= int(p):
            answer += 1
    return answer