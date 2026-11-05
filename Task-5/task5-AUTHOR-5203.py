from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'

ans = []
for N in range(1, 10_000):
    R = convert(N, 3)
    if sum(map(int, R)) % 3 == 0:
        R = '10' + R.replace('0', '*').replace('1', '0').replace('*', '1')
    else:
        R = '22' + R[2:] + '101'
    R = int(R, 3)
    if R > 314:
        ans.append([R, N])
min_R, min_N = min(ans)
print(min_N)