# with open(r'..\files\24_9753.txt') as file:
#     data = file.readline()
#
# l = r = cnt_y = ans = 0
# len_data = len(data)
#
# while r < len_data:
#     if cnt_y < 2:
#         if data[r] == 'Y':
#             cnt_y += 1
#         r += 1
#     else:
#         if data[l] == 'Y':
#             cnt_y -= 1
#         l += 1
#     ans = max(ans, r - l - (1 if r != len_data else 0))
#
# print(ans)

with open(r'..\files\24_9753.txt') as file:
    data = file.readline().strip()

l = 0
cnt_y = 0
ans = 0

for r in range(len(data)):
    if data[r] == 'Y':
        cnt_y += 1

    while cnt_y > 150:
        if data[l] == 'Y':
            cnt_y -= 1
        l += 1

    ans = max(ans, r - l + 1)

print(ans)