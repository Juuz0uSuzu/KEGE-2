# from string import printable
# def convert(num, sys):
#     res = ''
#     while num:
#         res += printable[num % sys]
#         num //= sys
#     return res[::-1] if res else '0'
#
# num = 6 * 144**26 + 11 * 12**75 - 48
# print(convert(num, 12).count('11'))

#########################################################

num = 6 * 144**26 + 11 * 12**75 - 48
cnt_B = 0
while num:
    if num % 12 == 11: cnt_B += 1
    num //= 12
print(cnt_B)