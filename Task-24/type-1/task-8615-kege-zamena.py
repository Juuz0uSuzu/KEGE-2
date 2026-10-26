with open(r'..\files\24_8615.txt')as file:
    s=file.readline()
for i in 'ABCDEF':
    s=s.replace(i,'B')
while 'BBB' in s:
    s=s.replace('BBB','BB BB')
s=s.split()
print(max(map(len, s)))