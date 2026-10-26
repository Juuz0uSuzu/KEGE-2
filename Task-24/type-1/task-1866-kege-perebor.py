file = open(r'..\files\24_1866.txt', 'r')
data=file.readline()
file.close()

cnt, ans = 1, 0

for i in range(len(data)-1):
    if data[i] + data[i+1] == 'a'or data[i:i+2] == 'd':
        ans = max(ans, cnt)
        cnt = 1
    else:
        cnt += 1
print(ans)