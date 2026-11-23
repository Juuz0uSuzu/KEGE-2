from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'

num =
print(convert(num, 14).count(''))

num =

cnt_11 = 0
cnt = 0

while num:
    if num % 14 == 11:
        cnt_11 += 1
    num //= 14

print(cnt)
