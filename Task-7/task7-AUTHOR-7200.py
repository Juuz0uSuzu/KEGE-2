from math import ceil, log2

width, height = 1280, 720
packs = 69
speed = 245760
min_time = 270

pixels = width * height

for N in range(1, 1000):
    i = ceil(log2(N))
    img_bytes = ceil(pixels * i / 8)

    if (img_bytes * packs) / speed > min_time:
        print(N)
        break