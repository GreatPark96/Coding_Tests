import itertools
def solution(nums):
    answer = 0
    combinations = list(itertools.combinations(nums,3))

    for num in combinations:
        chk = 0
        for i in range(2, int(sum(num)**0.5) + 1):
            if sum(num) % i == 0:
                chk += 1
                break
        if chk == 0:
            answer+= 1 
            
    return answer