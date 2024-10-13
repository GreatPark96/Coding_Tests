def solution(sizes):
    answer = 0
    w = 0
    h = 0
    
    for i in range(0, len(sizes)):
        sizes[i].sort()
        if w < min(sizes[i]):
            w = min(sizes[i])
        if h < max(sizes[i]):
            h = max(sizes[i])
    return w * h