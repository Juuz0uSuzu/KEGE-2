from turtle import *

screensize(10000, 10000)
tracer(0)
left(90)
k = 10

for i in range(2):
    fd(3 * k)
    rt(90)
    fd(20 * k)
    rt(90)
up()
bk(8 * k)
rt(90)
fd(9 * k)
lt(90)
down()
for i in range(2):
    fd(16 * k)
    rt(90)
    fd(8 * k)
    rt(90)
up()
for x in range(9, 18):
    for y in range(0, 4):
        teleport(x * k, y * k)
        dot(3, 'red')
print((20 + 1) * (3 + 1) + (16 + 1) * (8 + 1) - (18 - 9) * (4 - 0))
update()
done()
