from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'

num = 51 * 7**12 - 7**3 -22
z = (convert(num, 7))
print(sum(map(int, z)))