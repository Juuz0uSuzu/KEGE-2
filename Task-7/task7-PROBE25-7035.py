from math import ceil, log2

width, height = 1024, 768
colors = 4096
speed = 1310720
max_time = 300

i = ceil(log2(colors))
img_bits = width * height * i

ans = 0
for packs in range(1, 1000):
    if (img_bits * packs) / speed <= max_time:
        ans = packs
    else:
        break
print(ans)