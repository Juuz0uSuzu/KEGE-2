from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'

num = 7  * 729**543 - 6 * 81**765 - 5 * 9**987 - 20
print(convert(num, 9).count('8'))

#########################################################

num = 7  * 729**543 - 6 * 81**765 - 5 * 9**987 - 20
cnt_8 = 0
while num:
    if num % 9 == 8: cnt_8 += 1
    num //= 9
print(cnt_8)