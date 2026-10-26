with open(r'..\files\24_1273.txt', 'r') as file:
    data = file.readline()

# data ='***XYZ*****XYZ****************'

ans, cnt=0, 2
for line in zip(data, data[1:], data[2:]):
    if ''.join(line) != 'XYZ':
        cnt +=1
    else:
        cnt=2
    ans=max(ans, cnt)
print(ans)
