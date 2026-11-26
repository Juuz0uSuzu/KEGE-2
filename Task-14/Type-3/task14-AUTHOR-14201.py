ans = []
for x in range(1, 2031):
    num = 3 ** 100 - x
    cnt = 0
    while num:
        if num % 3 == 0:
            cnt +=1
        num //= 3
    ans.append([cnt, x])
print(max(ans))