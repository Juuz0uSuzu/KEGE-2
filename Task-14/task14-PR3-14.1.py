from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'

num = 5 * 216**3031 + 4 * 36**3042 - 3 * 6**3053 - 3064
z = (convert(num, 6))
print(sum(map(int, z)))