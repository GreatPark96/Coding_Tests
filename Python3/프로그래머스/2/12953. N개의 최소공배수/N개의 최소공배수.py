import math
def solution(arr):
    lcm = 0
    for i in range(0, len(arr)):
        if lcm == 0:
            lcm = arr[-1]
            arr.pop()
            continue
        lcm = lcm * arr[-1] // math.gcd(lcm,arr[-1])
        arr.pop()
        #1344
    return lcm
    