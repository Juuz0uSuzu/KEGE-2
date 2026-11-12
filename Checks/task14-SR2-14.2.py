from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'

num = 729**8 - 3**18 + 85
print(convert(num, 9).count('0'))

num = 729**8 - 3**18 + 85

cnt_0 = 0
while num:
    if num % 9 == 0: cnt_0 += 1
    num //= 9
print(cnt_0)