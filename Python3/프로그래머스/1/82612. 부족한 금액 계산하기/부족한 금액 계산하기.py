def solution(price, money, count):
    answer = -1
    
    pay = 0
    
    for i in range(1, count + 1):
        pay += price * i

    if (money - pay) >= 0:
        return 0
    else:
        return abs(money - pay)