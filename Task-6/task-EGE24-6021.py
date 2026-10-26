from turtle import *
screensize(10_000, 10_000)
tracer(0)
left(90)
k=10
for i in range(3):
    fd(7*k)
    rt(90)
    fd(12*k)
    rt(90)
up()
fd(4*k)
rt(90)
fd(6*k)
lt(90)
down()
for i in range(4):
    fd(83*k)
    rt(90)
    fd(77*k)
    rt(90)
up()
for x in range(0, 7):
    for y in range(0, 4):
        teleport(x*k, y*k)
        dot(3, 'red')
print((8*13)+(84*78)-(28))
update()
done()