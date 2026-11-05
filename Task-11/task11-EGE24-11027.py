from math import log2, ceil

for L in range(1, 10000):
    N = 52+10+458
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 862 <= 276*1024:
        print(L)






