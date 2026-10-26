from turtle import *
screensize(10_000, 10_000)
tracer(0)
left(90)
k=10
for i in range(2):
    fd(7*k)
    rt(90)
    fd(18*k)
    rt(90)
up()
bk(-2*k)
rt(90)
fd(9*k)
lt(90)
down()
for i in range(2):
    fd(8*k)
    rt(90)
    fd(5*k)
    rt(90)
up()
for x in range(9, 15):
    for y in range(2, 8):
        teleport(x*k, y*k)
        dot(3, 'red')
print((15-9)*(8-2))
update()
done()
