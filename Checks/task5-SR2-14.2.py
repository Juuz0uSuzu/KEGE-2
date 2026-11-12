from string import printable as alph
def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 1000):
    R = convert(N, 3)
    s = sum(map(int, R))
    if s % 3 == 0:
        R = R + '212'
    else:
        R = R + convert(s * 2, 3)
    R = int(R, 3)
    if R > 490:
        ans.append(R)
print(min(ans))