from math import log2, ceil

for L in range(1, 10000):
    N = 10 + 70
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 1_234_567 > 24*2**20:
        print(L)
        break





