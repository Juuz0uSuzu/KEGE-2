def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []
for N in range(1, 10_000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        s = sum(map(int, R)) * 2
        R = R + convert(s, 3)
    R = int(R, 3)
    if R > 520 and R % 2 != 0:
        ans.append(R)
print(min(ans))