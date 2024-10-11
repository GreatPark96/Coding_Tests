def solution(absolutes, signs):
    for i in range(0, len(absolutes)):
        mult = 1
        if not signs[i]:
             mult = -1   
        absolutes[i] = absolutes[i] * mult
    return sum(absolutes)
        