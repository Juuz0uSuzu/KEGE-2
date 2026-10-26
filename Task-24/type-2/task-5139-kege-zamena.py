with open(r'..\files\24_5139.txt') as file:
    data = file.readline()
sog = 'BCDF'
gl = 'AEU'

ans = cnt = i = 0
len_data = len(data) - 2
while i < len_data:
    if data[i] in sog and data[i+1] in gl and data[i+2] in sog:
        cnt += 1
        i += 3
        ans = max(ans, cnt)
    else:
        cnt = 0
        i += 1
print(ans)