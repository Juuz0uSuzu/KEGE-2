with open(r'..\files\24_1273.txt', 'r') as file:
    data = file.readline()

# data ='***XYZ*****XYZ****************'

ans, cnt=0, 2
for i in range(len(data) -2):
    if data[i:i+3] != 'XYZ':
        cnt +=1
    else:
        cnt=2
    ans=max(ans, cnt)
print(ans)
