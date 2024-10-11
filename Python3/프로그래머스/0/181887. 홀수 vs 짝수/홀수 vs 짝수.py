def solution(num_list):
    even =  sum(num_list[1::2]) # 짝수
    odd = sum(num_list[0::2]) # 홀수

    if even > odd:
        return even
    else:
        return odd