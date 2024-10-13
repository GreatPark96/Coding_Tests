def solution(s):
    answer = []
    for i in range(0, len(s)):
        if i == 0 or s[0:i].count(s[i]) == 0:
            answer.append(-1)
            continue
        backList = s[0:i]
        backList = backList[::-1]
        answer.append(backList.find(s[i]) + 1)
    return answer