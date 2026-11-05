from math import log2, ceil

for N in range(1, 10000):
    L = 248
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 75600 > 16*1024*1024:
        print(N)
        break
