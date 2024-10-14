# a : 마트에 주는 병 수
# b : a를 주면 주는 콜라 수
# n: 가져가는 빈병
def solution(a, b, n):
    bottel = n
    transCola = 0
    cola = 0

    while bottel >= a:
        transCola = (bottel // a) * b # 얻은 콜라
        bottel = (bottel % a) + transCola # 보유중인 콜라
        cola += transCola

    return cola