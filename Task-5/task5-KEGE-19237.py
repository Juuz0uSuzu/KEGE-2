def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []
for N in range(1, 10000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        sum_R = sum(map(int, R))
        R = R + convert(sum_R, 3)
    R = int(R, 3)
    if R > 220 and R % 2 == 0:
        ans.append(R)
print(min(ans))
#222