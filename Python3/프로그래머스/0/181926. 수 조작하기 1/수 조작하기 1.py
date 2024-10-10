def solution(n, control):
    answer = n
    for c in control:
        answer += {"w":1, "s": -1, "d": 10, "a": -10}.get(c, 0)
    return answer