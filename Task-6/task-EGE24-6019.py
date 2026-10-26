from turtle import *
screensize(10_000, 10_000)
tracer(0)
left(90)
k=10
for i in range(2):
    fd(21*k)
    rt(90)
    fd(27*k)
    rt(90)
up()
fd(9*k)
rt(90)
fd(10*k)
lt(90)
down()
for i in range(2):
    fd(86*k)
    rt(90)
    fd(47*k)
    rt(90)
up()
for x in range(10, 28):
    for y in range(10, 22):
        teleport(x*k, y*k)
        dot(3, 'red')
print((28-10)*(22-10))
update()
done()
