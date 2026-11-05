from string import printable


def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'


ans = []
for N in range(1, 10000):
    R = convert(N, 4)
    if sum(map(int, R)) % 2 == 0:
        R = R + R[-2:]
    else:
        R = '2' + R + '0'
    R = int(R, 4)
    if R > 120:
        ans.append(R)
print(min(ans))
