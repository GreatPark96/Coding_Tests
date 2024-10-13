def solution(number, limit, power):
    buyList = []
    
    for kisa in range(1, number + 1):
        count = 0
        interval = int(kisa ** 0.5)
        
        for j in range(1, interval + 1):
            if kisa % j == 0:
                if kisa == j**2:
                    count += 1
                else:
                    count += 2
        if count > limit:
            count = power
        
        buyList.append(count)
                
    return sum(buyList)