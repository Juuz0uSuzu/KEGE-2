with open(r'..\files\24_1866.txt', 'r') as file:
    s = file.readline()

max_len = 0
current_len = 0
prev = ''

for char in s:
    if (prev == 'a' and char == 'd') or (prev == 'd' and char == 'a'):
        current_len = 1
    else:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    prev = char

print(max_len)