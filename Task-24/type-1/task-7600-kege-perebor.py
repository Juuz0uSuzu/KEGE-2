with open(r'..\files\24_7600.txt', 'r') as file:
    s = file.readline()

bad = ('Q', 'R', 'S')

max_len = 0
current_len = 0
prev = ''

for char in s:
    if prev in bad and char in bad:
        current_len = 1
    else:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    prev = char

print(max_len)