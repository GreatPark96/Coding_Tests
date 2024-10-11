def solution(num):
    return {0: "Even"}.get(num % 2, "Odd")