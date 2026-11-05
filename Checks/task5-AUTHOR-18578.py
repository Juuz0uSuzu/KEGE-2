from string import printable as alph
def convert(num, sys):
    res = ''
    while num:
        res += alph[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 1000):
    R = convert(N, 4)
    if N % 4 == 0:
        R = '2' + R + '03'
    else:
        R += convert((N % 4) * 5, 4)
    R = int(R, 4)
    if R <= 567:
        ans.append(N)

print(max(ans))