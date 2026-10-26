with open(r'..\files\24_7853.txt', 'r') as file:
    s = file.readline()

bad = {'N', 'O', 'T'}

max_len = 0
current_len = 0
prev2 = ''
prev = ''

for char in s:
    if prev2 in bad and char in bad:
        current_len = 2
    else:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    prev2 = prev
    prev = char

print(max_len)