def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []
for N in range(10, 10000):  # N > 9
    R = convert(N, 3)
    if N % 2 == 0:
        R += R[-2:]
    else:
        summa = sum(map(int, R))
        R += convert(summa, 3)

    R = int(R, 3)
    ans.append([R, N])

print(min(ans)[1])