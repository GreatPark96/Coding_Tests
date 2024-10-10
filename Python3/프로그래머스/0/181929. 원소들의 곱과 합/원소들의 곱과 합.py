def solution(num_list):
    sum = 0
    mult = 1
    for num in num_list:
        sum += num
        mult *= num
    if pow(sum,2) > mult:
        return 1
    else:
        return 0