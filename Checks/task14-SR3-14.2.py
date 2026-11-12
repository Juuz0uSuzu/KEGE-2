from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1] if res else '0'

num = 283**382 + 9**15 + 2**3
print(abs(convert(num, 14).count('b') - convert(num, 14).count('c')))

num = 283**382 + 9**15 + 2**3

cnt_11 = 0
cnt_12 = 0

while num:
    if num % 14 == 11:
        cnt_11 += 1
    if num % 14 == 12:
        cnt_12 += 1
    num //= 14

print(abs(cnt_11 - cnt_12))
