import collections

def solution(k, tangerine):
    sum = 0
    count = collections.Counter(tangerine)
    countSort = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    categ = 0
    
    for key, value in countSort.items():
        categ += 1
        for i in range(0, value):
            sum += 1
            if sum >= k:
                return categ
        
        