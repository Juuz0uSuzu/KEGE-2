from math import log2, ceil

for L in range(1, 10000):
    N = 52 + 10 + 963
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 2000 <= 693*1024:
        print(L)
