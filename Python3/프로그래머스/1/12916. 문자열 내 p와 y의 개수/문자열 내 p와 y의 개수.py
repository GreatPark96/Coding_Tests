def solution(s):
    str = s.lower()
    pCount = 0 
    yCount = 0
    
    for c in str:
        if c == 'p':
            pCount += 1
        elif c == 'y':
            yCount += 1
    if pCount == yCount:
        return True
    else:
        return False
        