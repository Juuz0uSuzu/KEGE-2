with open(r'..\files\24_4682.txt') as file:
    data = file.readline()
for i in 'AB', 'AC', 'AD', 'EB', 'EC', 'ED':
    data= data.replace(i, '*')

for i in 'ABCDE':
    data= data.replace(i, ' ')


data=data.split()

print(len(max(data, key=len)))