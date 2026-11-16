from math import log2, ceil

for L in range(1, 10000):
    N = 10 + 26 + 34
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 1142 > 305*1024 :
        print(L)
        break