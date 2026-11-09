def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1] if res else '0'

ans = []
for N in range(1, 10000):
    R = convert(N, )
    R = int(R, )
    if R :
        ans.append()
print(min(ans))
#222