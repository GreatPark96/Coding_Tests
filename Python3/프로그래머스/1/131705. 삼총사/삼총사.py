def solution(number):
    datas = []
    answer = 0
    for i in range(0, len(number)):
        for j in range(i + 1, len(number)):
            for k in range(j + 1, len(number)):
                datas.append([number[i], number[j], number[k]])
    for data in datas:
        if sum(data) == 0:
            answer += 1
    return answer