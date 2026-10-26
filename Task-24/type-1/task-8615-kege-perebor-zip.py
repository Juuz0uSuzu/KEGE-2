from itertools import product

with open(r'..\files\24_8615.txt', 'r') as file:
    data = file.readline()
combs= list(product('ABCDEF', repeat=3))
ans, cnt=0, 2
for line in zip(data, data[1:], data[2:]):
    if line not in combs:
        cnt +=1
    else:
        cnt=2
    ans=max(ans, cnt)
print(ans)
