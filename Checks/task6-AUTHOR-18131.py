from turtle import *
screensize(10000, 10000)
tracer(0)
left(90)
k=10
for i in range(9):
    fd(22*k)
    rt(90)
    fd(6*k)
    rt(90)
up()
fd(1*k)
rt(90)
fd(5*k)
lt(90)
down()
for i in range(9):
    fd(53*k)
    rt(90)
    fd(75*k)
    rt(90)
up()
for x in range(0, 2):
    for y in range(0, 22):
        teleport(x*k, y*k)
        dot(3, 'red')
print((2 - 0) * (22 - 0))
update()
done()
