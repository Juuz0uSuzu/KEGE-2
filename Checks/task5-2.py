def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'


ans = []
for N in range(1, 10000):
    R = convert(N, 2)

    if N % 8 == 0:
        R += R[-2:]
    else:
        ostatok = (N % 8) * 2
        R += convert(ostatok, 2)

    R = int(R, 2)

    if R > 3000:
        ans.append(N)

print(min(ans))