import math


for n in range(1,1000000):
    s = math.floor(math.sqrt(n))
    factor_before = factor_after =  False
    for i in range(2,s+1):
        if n % i == 0:
            factor_before = True
            break

    for i in range(s+1, n//2 + 1):
        if n % i == 0:
            factor_after = True
            break

    if (not factor_before) and factor_after:
        print(n)





