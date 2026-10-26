from turtle import *
screensize(10_000, 10_000)
tracer(0)
left(90)
k=50
rt(30)
for i in range(3):
    rt(150)
    fd(6*k)
    rt(30)
    fd(12*k)
up()
for x in range(-6, 1):
    for y in range(-16, 1):
        teleport(x*k, y*k)
        dot(3, 'red')
update()
done()