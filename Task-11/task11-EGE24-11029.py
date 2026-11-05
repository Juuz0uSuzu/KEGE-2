from math import log2, ceil

for L in range(1, 10000):
    N = 26 + 10 + 450
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 708 > 213*1024:
        print(L)
        break
