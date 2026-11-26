from turtle import *

screensize(10_000, 10_000)
tracer(0)
k = 10
left(90)

for i in range(3):
    fd(27 * k)
    rt(90)
    fd(12 * k)
    rt(90)
up()
fd(4 * k)
rt(90)
fd(6 * k)
lt(90)
down()
for i in range(4):
    fd(83 * k)
    rt(90)
    fd(77 * k)
    rt(90)
up()
for x in range(0, 7):
    for y in range(0, 24):
        teleport(x * k, y * k)
        dot(3, 'red')
print((27 + 1) * (12 + 1) + (83 + 1) * (77 + 1) - (7 - 0) * (24 - 0))
update()
done()
