import itertools

def solution(lottos, win_nums):
    answer = []
    number = [i for i in range(1, 46)]
    score = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    
    if lottos.count(0) == 0:
        top = list(set(lottos) & set(win_nums))
        top = score[len(top)]
        return [top, top]
    
    zero = lottos.count(0)
    
    top = list(set(lottos) & set(win_nums))
    top = score[len(top) + zero]
    
    low = list(set(lottos) & set(win_nums))
    low =  score[len(low)]
    
    return [top, low]
    