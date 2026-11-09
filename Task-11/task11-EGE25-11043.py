from math import log2, ceil

for L in range(1, 10000):
    N = 52 + 10 + 500
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 45877 > 49*1024*1024 :
        print(L)
        break





