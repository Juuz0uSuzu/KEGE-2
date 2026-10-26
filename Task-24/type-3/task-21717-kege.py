with open(r'..\files\24_21717.txt') as file:
    data=file.readline()
data=data.split('RSQ')
ans=10**10
for i in range(1, len(data) - 128 - 1):
    line='RSQ'+'RSQ'.join(data[i:i+129])+'RSQ'
    next_line=data[i+129]
    for j in range(len(next_line)):
        if next_line[j] != 'Q':
            ans = min(ans, len(line)+j+1)
            break
    else:
        ans = min(ans, len(line) + len(next_line) +1)
print(ans)