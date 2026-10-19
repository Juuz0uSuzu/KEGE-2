from turtle import *
tracer(0)
screensize(10000, 10000)
left(90)
k=10
for i in range(3):
    fd(39*k)
    rt(90)
    fd(48*k)
    rt(90)
up()
fd(27*k)
rt(90)
fd(24*k)
lt(90)
down()
for i in range(3):
    fd(29*k)
    rt(90)
    bk(18*k)
    rt(90)
up()
for x in range(24, 43):
    for y in range(0, 13):
        teleport(x*k, y*k)
        dot(3, 'red')
print((39*48)+(29*18)-(43-24-1)*(13-0-1))
update()
done()