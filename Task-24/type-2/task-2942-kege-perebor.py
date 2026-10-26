with open(r'..\files\24_2942.txt', 'r') as file:
    data = file.readline()

ans=cnt=i=0
len_data=len(data)-1
while i<len_data:
    if data[i:i+2] in 'AB AC':
        cnt+=1
        i+=2
        ans = max(ans, cnt)
    else:
        cnt=0
        i += 1
print(ans)