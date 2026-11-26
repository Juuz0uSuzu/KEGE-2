from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'

num = 11 * 15**65 + 18 * 15**38 - 14 * 15**17 + 19 * 15**11 + 18338
z = (convert(num, 15))
print(len(set(z)))

#########################################################
num = 11 * 15**65 + 18 * 15**38 - 14 * 15**17 + 19 * 15**11 + 18338
res = set()
while num:
    res.add(num % 15)
    num //= 15
print(len(res))