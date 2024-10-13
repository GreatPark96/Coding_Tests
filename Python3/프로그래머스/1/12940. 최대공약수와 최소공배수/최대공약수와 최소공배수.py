def solution(n, m):
    gcd = 0
    
    # 최대공약수
    for i in range(max([n,m]), 0, -1):
        if n % i == 0 and m % i == 0:
            gcd = i
            break
    
    return [gcd, n * m / gcd]
    