# n : 페인트가 칠해진 길이
# m : 롤러의 길이
# section : 구역
# 롤러로 페인트를 칠하는 횟수

def solution(n, m, section):
    answer = 0;
    distance = 0;
    for i in range(0, len(section)): 
        if section[i] <= distance:
            continue;
        distance = section[i] + m - 1;
        answer += 1;
    return answer
    