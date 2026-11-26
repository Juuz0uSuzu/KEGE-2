from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'

num = 16**820 - 2**761 + 14
print(convert(num, 4).count('0'))