from turtle import *

screensize(10_000, 10_000)
tracer(0)
left(90)
k = 10
for i in range(5):
    fd(13 * k)
    rt(90)
    fd(5 * k)
up()
rt(90)
fd(10 * k)
lt(90)
fd(7 * k)
down()
for i in range(2):
    fd(8 * k)
    rt(90)
    fd(11 * k)
    rt(90)
up()
for x in range(12, 19):
    for y in range(-5, 4):
        teleport(x * k, y * k)
        dot(3, 'red')
# (S1 * S2) + (S3 * S4) - (R1 - L1 -1) * (R2 - L2 -1)
print((18 * 18) + (8 * 11) - (19 - 12 - 1) * (4 - (-5) - 1))
update()
done()
